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


class PembejeoApiView(APIView):
    def get(self, request):

        pembejeos = Pembejeo.objects.all()
        serializer = PembejeoSerializer(pembejeos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data 
        serializer = PembejeoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TargetApiView(APIView):

    def get(self, request):
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):

        data = request.data 
        serializer = TargetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

            target_obj = get_object_or_404(Target, id=data['target_id'])

            if target_obj.name == 'Pembejeo':

                pembejeo_obj = get_object_or_404(Pembejeo, id=data['pembejeo_id'])                
                 
                obj = Feedback(
                    name = data['name'],
                    phone = data['phone'],
                    location = data['location'],
                    target = target_obj,
                    pembejeo = pembejeo_obj,
                    description = data['description'],
                )
                obj.save()

                # send email
                subject = 'Mkulima Digital'
                html_message = render_to_string('mail/mail_template.html', {
                    'name':obj.name,
                    'phone':obj.phone,
                    'location':obj.location,
                    'target':target_obj, 
                    'pembejeo':pembejeo_obj,
                    'description':obj.description,               
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
                    target = target_obj,
                )
                obj.save()

                # send email
                subject = 'Mkulima Digital'
                html_message = render_to_string('mail/mail_template.html', {
                    'name':obj.name,
                    'phone':obj.phone,
                    'location':obj.location,
                    'target':target_obj,                
                })
                plain_message = strip_tags(html_message)
                recipient_list = ['info@agriwezesha.co.tz','agriwezesha@gmail.com',]
                from_email = "mkulimadigital@agriwezesha.co.tz"
                mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
