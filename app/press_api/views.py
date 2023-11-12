from django.db.models import F, Sum
from rest_framework import generics

from press.models import Gender, Journalist, Press, models

from .serializers import GenderSerializer, PressSerializer


class MalePressRanking(generics.ListAPIView):
    queryset = Press.objects.all()
    serializer_class = PressSerializer

    def get_queryset(self):
        queryset = Press.objects.annotate(
            male_subscriber_count=Sum(
                F("journalist__subscriber_count")
                * F("journalist__gender__percentage")
                / 100,
                output_field=models.IntegerField(),
                filter=models.Q(journalist__gender__gender="M"),
            )
        ).order_by("-male_subscriber_count")[:10]

        return queryset


class FemalePressRanking(generics.ListAPIView):
    queryset = Press.objects.all()
    serializer_class = PressSerializer

    def get_queryset(self):
        queryset = Press.objects.annotate(
            male_subscriber_count=Sum(
                F("journalist__subscriber_count")
                * F("journalist__gender__percentage")
                / 100,
                output_field=models.IntegerField(),
                filter=models.Q(journalist__gender__gender="F"),
            )
        ).order_by("-male_subscriber_count")[:10]
        return queryset


class JournalistGenderDetail(generics.ListAPIView):
    queryset = Journalist.objects.all()
    serializer_class = GenderSerializer

    def get_queryset(self):
        journalist_id = self.kwargs.get("pk")
        queryset = Gender.objects.filter(journalist_id=journalist_id)
        return queryset
