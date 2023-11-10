from rest_framework import generics
from .serializer import *
from django.db.models import Sum
from press.models import *


class PressList(generics.ListCreateAPIView):
    queryset = Press.objects.annotate(subscriber_count = Sum('journalist__subscribers_count'), cheer_count = Sum('journalist__cheer_count'))
    serializer_class = PressSerializer


class PressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Press.objects.annotate(subscriber_count = Sum('journalist__subscribers_count'), cheer_count = Sum('journalist__cheer_count'))
    serializer_class = PressSerializer
    lookup_field = 'name'
    



class PressJournallist(generics.ListAPIView):
    serializer_class = JournalistSeriallizer



    def get_queryset(self):
        qs = Journalist.objects.all()
        return qs.filter(press__name=self.kwargs['press_name'])


class PressRanking(generics.ListCreateAPIView):
    serializer_class = PressSerializer
    
    
    def get_queryset(self):
        number = self.request.GET.get('number', 10)
        number = int(number)
        qs = Press.objects.annotate(subscriber_count = Sum('journalist__subscribers_count'), cheer_count = Sum('journalist__cheer_count')).order_by('-subscriber_count')[:number]
        return qs


class PressJournallistRanking(generics.ListAPIView):
    serializer_class = JournalistSeriallizer


    def get_queryset(self):
        number = self.request.GET.get('number', 10)
        number = int(number)
        qs = Journalist.objects.all()
        return qs.filter(press__name=self.kwargs['press_name']).order_by('-subscribers_count')[:number]


class JournalistRanking(generics.ListCreateAPIView):
    serializer_class = JournalistSeriallizer
  
    def get_queryset(self):
        number = self.request.GET.get('number', 10)
        number = int(number)
        qs = Journalist.objects.all()
        return qs.order_by('-subscribers_count')[:number]

