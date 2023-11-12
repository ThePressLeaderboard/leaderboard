from rest_framework import serializers

from press.models import Gender, Journalist, Press


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"
        read_only_fields = ("id",)


class JournalistsSerializer(serializers.ModelSerializer):
    Gender = GenderSerializer(many=True, read_only=True)

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
