from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import *
from .serializers import *

from django.conf import settings




class FeedbackApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):

        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):

        # logic
        data = request.data 
        
        serializer = FeedbackSerializer(data=data)

        if serializer.is_valid():

            
            if data['target'] == 1:                              
                 
                obj = Feedback(
                    name = data['name'],
                    phone = data['phone'],
                    location = data['location'],
                    target = data['target'],
                    pembejeo_type = data['pembejeo_type'],                
                    pembejeo_desc = data['pembejeo_desc']                    
                )
                obj.save()

                # send email
                subject = 'Mkulima Digital'
                html_message = render_to_string('mail/mail_template.html', {
                    'name':obj.name,
                    'phone':obj.phone,
                    'location':obj.location,
                    'target':'Pembejeo',
                    'pembejeo_type' : obj.pembejeo_type,                                    
                    'pembejeo_desc':obj.pembejeo_desc,                               
                })
                plain_message = strip_tags(html_message)
                recipient_list = ['info@agriwezesha.co.tz','agriwezesha@gmail.com',]
                from_email = "mkulimadigital@agriwezesha.co.tz"
                mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)
            else:
                obj = Feedback(
                    name = data['name'],
                    phone = data['phone'],
                    location = data['location'],
                    target =data['target'],                    
                    ushauri_desc = data['ushauri_desc']                   
                )
                obj.save()

                # send email
                subject = 'Mkulima Digital'
                html_message = render_to_string('mail/mail_template.html', {
                    'name':obj.name,
                    'phone':obj.phone,
                    'location':obj.location,
                    'target':'Huduma za Kitalaamu',
                    'ushauri_desc':obj.ushauri_desc             
                })
                plain_message = strip_tags(html_message)
                recipient_list = ['info@agriwezesha.co.tz','agriwezesha@gmail.com',]
                from_email = "mkulimadigital@agriwezesha.co.tz"
                mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
