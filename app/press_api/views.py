from rest_framework import generics
from .serializer import *
from django.db.models import Sum
from press.models import *

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.annotate(subscriber_count = Sum('press__journalist__subscribers_count'))
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(subscriber_count = Sum('press__journalist__subscribers_count'))
    serializer_class = CategorySerializer
    lookup_field = 'category_name'


class CategoryPress(generics.ListAPIView):
    serializer_class = PressSerializer


    def get_queryset(self):
        qs = Press.objects.annotate(subscriber_count = Sum('journalist__subscribers_count'))
        qs = qs.filter(category__category_name=self.kwargs['category_name'])
        return qs


class CategoryJournalist(generics.ListAPIView):
    serializer_class = JournalistSeriallizer


    def get_queryset(self):
        qs = Journalist.objects.filter(press__category__category_name=self.kwargs['category_name'])
        return qs
    

class PressList(generics.ListCreateAPIView):
    queryset = Press.objects.annotate(subscriber_count = Sum('journalist__subscribers_count'))
    serializer_class = PressSerializer


class PressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Press.objects.annotate(subscriber_count = Sum('journalist__subscribers_count'))
    serializer_class = PressSerializer
    lookup_field = 'name'
    

class PressJournallist(generics.ListAPIView):
    serializer_class = JournalistSeriallizer


    def get_queryset(self):
        qs = Journalist.objects.filter(press__name=self.kwargs['press_name'])
        return qs


class CategoryRanking(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    
    
    def get_queryset(self):
        number = self.request.GET.get('number', 10)
        number = int(number)
        qs = Category.objects.annotate(subscriber_count = Sum('press__journalist__subscribers_count')).order_by('-subscriber_count')[:number]
        return qs


class CategoryPressRanking(generics.ListAPIView):
    serializer_class = PressSerializer


    def get_queryset(self):
        number = self.request.GET.get('number', 10)
        number = int(number)
        qs = Press.objects.filter(category__category_name=self.kwargs['category_name'])
        qs = qs.annotate(subscriber_count = Sum('journalist__subscribers_count')).order_by('-subscriber_count')[:number]
        return qs

class CategoryJournalistRanking(generics.ListAPIView):
    serializer_class = JournalistSeriallizer


    def get_queryset(self):
        number = self.request.GET.get('number', 10)
        number = int(number)
        qs = Journalist.objects.filter(press__category__category_name=self.kwargs['category_name']).order_by('-subscribers_count')[:number]
        return qs


class PressRanking(generics.ListCreateAPIView):
    serializer_class = PressSerializer
    
    
    def get_queryset(self):
        number = self.request.GET.get('number', 10)
        number = int(number)
        qs = Press.objects.annotate(subscriber_count = Sum('journalist__subscribers_count')).order_by('-subscriber_count')[:number]
        return qs


class PressJournallistRanking(generics.ListAPIView):
    serializer_class = JournalistSeriallizer


    def get_queryset(self):
        number = self.request.GET.get('number', 10)
        number = int(number)
        qs = Journalist.objects.filter(press__name=self.kwargs['press_name']).order_by('-subscribers_count')[:number]
        return qs


class JournalistRanking(generics.ListCreateAPIView):
    serializer_class = JournalistSeriallizer
    

    def get_queryset(self):
        number = self.request.GET.get('number', 10)
        number = int(number)
        qs = Journalist.objects.all().order_by('-subscribers_count')[:number]
        return qs