from rest_framework import serializers
from press.models import Category, Press, Journalist, Age, Section, JournalistSection


class PressSerializer(serializers.ModelSerializer):
    subscriber_count = serializers.IntegerField()
    cheer_count = serializers.IntegerField()
    male_subscriber = serializers.IntegerField()
    female_subscriber = serializers.IntegerField()

    class Meta:
        model = Press
        fields = (
            "category",
            "press_name",
            "subscriber_count",
            "cheer_count",
            "male_subscriber",
            "female_subscriber",
        )


class CategorySerializer(serializers.ModelSerializer):
    subscriber_count = serializers.IntegerField()
    cheer_count = serializers.IntegerField()
    male_subscriber = serializers.IntegerField()
    female_subscriber = serializers.IntegerField()

    class Meta:
        model = Category
        fields = (
            "category_name",
            "subscriber_count",
            "cheer_count",
            "male_subscriber",
            "female_subscriber",
        )



class JournalistSerializer(serializers.ModelSerializer):
    male_subscriber = serializers.IntegerField()
    female_subscriber = serializers.IntegerField()

    class Meta:
        model = Journalist
        fields = (
            "press",
            "journalist_id",
            "name",
            "subscriber_count",
            "article_count",
            "cheer_count",
            "male_subscriber",
            "female_subscriber",
        )


class PressSubscriberAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Age
        fields = ["age", "percentage", "journalist_id"]


class SectionSerializer(serializers.ModelSerializer):
    subscriber_count = serializers.IntegerField()
    cheer_count = serializers.IntegerField()
    male_subscriber = serializers.IntegerField()
    female_subscriber = serializers.IntegerField()

    class Meta:
        model = Section
        fields = (
            "section_name",
            "subscriber_count",
            "cheer_count",
            "male_subscriber",
            "female_subscriber",
        )


class PressJournalistSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalistSection
        fields = ["id", "journalist_id", "section_name"]


class PressRankingSerializer(serializers.Serializer):
    press_name = serializers.CharField()
    count = serializers.IntegerField()


class AgeRankingByCategorySerializer(serializers.Serializer):
    age_group = serializers.CharField()
    press_ranking = PressRankingSerializer(many=True)


class PressAgeSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    total_subscribers = serializers.IntegerField()
