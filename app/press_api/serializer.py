from rest_framework import serializers
from press.models import Category, Press, Journalist


class CategorySerializer(serializers.ModelSerializer):
    subscriber_count = serializers.IntegerField()
    
    
    class Meta:
        model = Category
        fields = '__all__'


class PressSerializer(serializers.ModelSerializer):
    subscriber_count = serializers.IntegerField()

    class Meta:
        model = Press
        fields = '__all__'


class JournalistSeriallizer(serializers.ModelSerializer):

    class Meta:
        model = Journalist
        fields = '__all__'
