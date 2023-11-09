from rest_framework import serializers
from .models import *


class SubscribersGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribersGender
        fields = "__all__"
        read_only_fields = ("id",)


class JournalistsSerializer(serializers.ModelSerializer):
    SubscribersGender = SubscribersGenderSerializer(many=True, read_only=True)
    class Meta:
        model = Journalist
        fields = "__all__"
        read_only_fields = ("id",)


class PressSerializer(serializers.ModelSerializer):
    Journalists = JournalistsSerializer(many=True, read_only=True)
    class Meta:
        model = Press
        fields = "__all__"
        read_only_fields = ("id",) 
