from django.db.models import F, Case, Sum, Value, When
from django.shortcuts import render
from django.db.models.functions import Coalesce
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from press.models import (
    Category,
    Press,
    Journalist,
    Age,
    models,
)
from press_api.serializer import (
    AgeRankingByCategorySerializer,
    CategorySerializer,
    PressSerializer,
    JournalistSerializer,
    PressSubscriberAgeSerializer,
    PressAgeSerializer,
    CategorySerializer,
    PressSerializer,
    SectionSerializer,
)
from rest_framework.pagination import PageNumberPagination

from .queryset import (
    category_query_set,
    journalist_query_set,
    press_query_set,
    secion_query_set,
)

from .pagination import PostPageNumberPagination


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
    serializer_class = JournalistSerializer
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
    serializer_class = JournalistSerializer
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
    serializer_class = JournalistSerializer
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
    serializer_class = JournalistSerializer
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
    serializer_class = JournalistSerializer
    lookup_field = "journalist_id"


class SubscriberAgeList(generics.ListCreateAPIView):
    queryset = Age.objects.all()
    serializer_class = PressSubscriberAgeSerializer
    pagination_class = PostPageNumberPagination


class SubscriberAgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Age.objects.all()
    serializer_class = PressSubscriberAgeSerializer
    pagination_class = PostPageNumberPagination

    def get_queryset(self):
        journalist_id = self.kwargs["journalist_id"]
        queryset = Age.objects.filter(journalist_id=journalist_id)
        return queryset


class SubscribersAgeByPressName(generics.ListAPIView):
    serializer_class = PressSubscriberAgeSerializer
    pagination_class = PostPageNumberPagination

    def get_queryset(self):
        press_name = self.kwargs["press_name"]  # URL에서 press_name을 가져옴
        queryset = Age.objects.filter(journalist__press__press_name=press_name)
        return queryset


class AgePressRanking(generics.ListAPIView):
    serializer_class = AgeRankingByCategorySerializer
    pagination_class = PostPageNumberPagination

    def get_queryset(self):
        age_ranges = [10, 20, 30, 40, 50, 60]
        result = []

        for age_range in age_ranges:
            age_group = f"{age_range}대"
            press_ranking = []

            for press in Press.objects.all():
                press_name = press.press_name
                age_subscriber_count = self.get_age_subscriber_count(press, age_range)

                press_ranking.append(
                    {"press_name": press_name, "count": age_subscriber_count}
                )

            press_ranking = sorted(
                press_ranking, key=lambda x: x["count"], reverse=True
            )
            press_ranking = press_ranking[:5]
            result.append({"age_group": age_group, "press_ranking": press_ranking})

        return result

    def get_age_subscriber_count(self, press, age_range):
        age_subscriber_count = (
            Press.objects.filter(id=press.id)
            .annotate(
                age_subscriber_count=Coalesce(
                    Sum(
                        Case(
                            When(
                                journalist__age__age=age_range,
                                then=F("journalist__subscriber_count")
                                * F("journalist__age__percentage")
                                / 100,
                            ),
                            default=Value(0),
                            output_field=models.IntegerField(),
                        )
                    ),
                    Value(0),
                )
            )
            .values_list("age_subscriber_count", flat=True)
            .first()
        )

        return age_subscriber_count

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryWiseAgePressRanking(APIView):
    paginatoin_class = PostPageNumberPagination

    def get(self, request):
        age = request.query_params.get("age")

        if age is not None:
            age_ranges = [int(age)]
        else:
            age_ranges = [10, 20, 30, 40, 50, 60]

        result = []

        for age_range in age_ranges:
            age_group = f"{age_range}대"
            age_ranking = []

            for category in Category.objects.all():
                category_name = category.category_name
                age_press_ranking = (
                    Press.objects.annotate(
                        age_subscriber_count=Coalesce(
                            Sum(
                                Case(
                                    When(
                                        journalist__age__age=age_range,
                                        then=F("journalist__subscriber_count")
                                        * F("journalist__age__percentage")
                                        / 100,
                                    ),
                                    default=Value(0),
                                    output_field=models.IntegerField(),
                                )
                            ),
                            Value(0),
                        )
                    )
                    .filter(category=category)
                    .order_by("-age_subscriber_count")[:5]
                )

                category_ranking = {
                    "category_name": category_name,
                    "press_ranking": [
                        {
                            "press_name": press.press_name,
                            "count": press.age_subscriber_count,
                        }
                        for press in age_press_ranking
                    ],
                }

                age_ranking.append(category_ranking)

            age_group_ranking = {"age_group": age_group, "categories": age_ranking}
            result.append(age_group_ranking)

        return Response(result)


class TotalAgeByPress(generics.RetrieveAPIView):
    serializer_class = PressAgeSerializer

    def get_queryset(self):
        press_name = self.kwargs.get("press_name").upper()
        return Age.objects.filter(journalist__press__press_name=press_name)

    def retrieve(self, request, *args, **kwargs):
        press_name = self.kwargs.get("press_name").upper()
        queryset = self.get_queryset()
        age_ranges = [10, 20, 30, 40, 50, 60]
        result = []
        result.append({"press_name": press_name})

        for age_range in age_ranges:
            age_group = f"{age_range}대"
            total_subscribers = queryset.filter(age=age_range).aggregate(
                total=Sum("percentage")
            )["total"]
            result.append(
                {"age_group": age_group, "total_subscribers": total_subscribers}
            )

        return Response(result)
