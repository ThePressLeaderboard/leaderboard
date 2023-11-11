from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .queryset import (
    category_query_set,
    journalist_query_set,
    press_query_set,
    secion_query_set,
)
from .serializer import (
    CategorySerializer,
    JournalistSeriallizer,
    PressSerializer,
    SectionSerializer,
)


class CategoryRanking(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = category_query_set.order_by(sort)[:number]
        return qs


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = category_query_set
    serializer_class = CategorySerializer
    lookup_field = "category_name"


class CategoryPressRanking(generics.ListAPIView):
    serializer_class = PressSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 10)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = press_query_set
        qs = qs.filter(category__category_name=self.kwargs["category_name"]).order_by(
            sort
        )[:number]
        return qs


class CategoryJournalistRanking(generics.ListAPIView):
    serializer_class = JournalistSeriallizer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = journalist_query_set
        qs = qs.filter(
            press__category__category_name=self.kwargs["category_name"]
        ).order_by(sort)[:number]
        return qs


class PressRanking(generics.ListCreateAPIView):
    serializer_class = PressSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = press_query_set.order_by(sort)[:number]
        return qs


class PressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = press_query_set
    serializer_class = PressSerializer
    lookup_field = "press_name"


class PressJournallistRanking(generics.ListAPIView):
    serializer_class = JournalistSeriallizer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = journalist_query_set
        qs = qs.filter(press__press_name=self.kwargs["press_name"]).order_by(sort)[
            :number
        ]
        return qs


class SectionRanking(generics.ListCreateAPIView):
    serializer_class = SectionSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = secion_query_set.order_by(sort)[:number]
        return qs


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = secion_query_set
    serializer_class = SectionSerializer
    lookup_field = "section_name"


class SectionJournallistRanking(generics.ListAPIView):
    serializer_class = JournalistSeriallizer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = journalist_query_set
        qs = qs.filter(
            journalistsection__section__section_name=self.kwargs["section_name"]
        ).order_by(sort)[:number]
        return qs


class JournalistRanking(generics.ListCreateAPIView):
    serializer_class = JournalistSeriallizer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = journalist_query_set.order_by(sort)[:number]
        return qs


class JournalistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = journalist_query_set
    serializer_class = JournalistSeriallizer
    lookup_field = "journalist_id"
