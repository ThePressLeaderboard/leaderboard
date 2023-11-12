from rest_framework import serializers
from press.models import Category, Press, Journalist, Age, Section, JournalistSection


class PressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ["press_name", "category"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_name"]


class JournalistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journalist
        fields = [
            "journalist_id",
            "name",
            "subscriber_count",
            "article_count",
            "cheer_count",
            "press",
        ]


class PressSubscriberAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Age
        fields = ["age", "percentage", "journalist_id"]


class PressSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ["section_name"]


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
