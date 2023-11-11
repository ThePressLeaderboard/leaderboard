from rest_framework import serializers
from press.models import Category, Press, Section, Journalist


class CategorySerializer(serializers.ModelSerializer):
    subscriber_count = serializers.IntegerField()
    cheer_count = serializers.IntegerField()
    male_subscriber = serializers.IntegerField()
    female_subscriber = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('category_name', 'subscriber_count', 'cheer_count', 'male_subscriber', 'female_subscriber')


class PressSerializer(serializers.ModelSerializer):
    subscriber_count = serializers.IntegerField()
    cheer_count = serializers.IntegerField()
    male_subscriber = serializers.IntegerField()
    female_subscriber = serializers.IntegerField()

    class Meta:
        model = Press
        fields = ('category', 'press_name', 'subscriber_count', 'cheer_count', 'male_subscriber', 'female_subscriber')


class SectionSerializer(serializers.ModelSerializer):
    subscriber_count = serializers.IntegerField()
    cheer_count = serializers.IntegerField()
    male_subscriber = serializers.IntegerField()
    female_subscriber = serializers.IntegerField()

    class Meta:
        model = Section
        fields = ('section_name', 'subscriber_count', 'cheer_count', 'male_subscriber', 'female_subscriber')


class JournalistSeriallizer(serializers.ModelSerializer):
    male_subscriber = serializers.IntegerField()
    female_subscriber = serializers.IntegerField()

    class Meta:
        model = Journalist
        fields = ('press', 'journalist_id', 'name', 'subscriber_count', 'article_count',
                  'cheer_count', 'male_subscriber', 'female_subscriber')
