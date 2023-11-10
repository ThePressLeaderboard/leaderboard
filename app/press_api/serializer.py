from rest_framework import serializers
from press.models import Press, Journalist


class PressSerializer(serializers.ModelSerializer):
    subscriber_count = serializers.IntegerField()
    cheer_count = serializers.IntegerField()

    class Meta:
        model = Press
        fields = '__all__'


class JournalistSeriallizer(serializers.ModelSerializer):

    class Meta:
        model = Journalist
        fields = '__all__'
