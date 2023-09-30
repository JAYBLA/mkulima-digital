from rest_framework import serializers
from .models import *


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["id", "name", "phone", "location",  "target","pembejeo_type","pembejeo_desc", "ushauri_desc"]