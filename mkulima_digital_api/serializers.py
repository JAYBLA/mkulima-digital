from rest_framework import serializers
from .models import *

class TargetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Target
        fields = ['id', 'name',]

class PembejeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pembejeo
        fields = ['id', 'name',]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["id", "name", "phone", "location",  "description", ]