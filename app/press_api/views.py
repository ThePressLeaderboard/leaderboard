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
from press_api.serializers import (
    AgeRankingByCategorySerializer,
    CategorySerializer,
    PressSerializer,
    JournalistSerializer,
    PressSubscriberAgeSerializer,
    PressAgeSerializer,
)
from .pagination import PostPageNumberPagination


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PostPageNumberPagination


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PostPageNumberPagination


class PressList(generics.ListCreateAPIView):
    queryset = Press.objects.all()
    serializer_class = PressSerializer
    pagination_class = PostPageNumberPagination


class PressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Press.objects.all()
    serializer_class = PressSerializer
    pagination_class = PostPageNumberPagination


class JournalistList(generics.ListCreateAPIView):
    queryset = Journalist.objects.all()
    serializer_class = JournalistSerializer
    pagination_class = PostPageNumberPagination


class JournalistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journalist.objects.all()
    serializer_class = JournalistSerializer
    pagination_class = PostPageNumberPagination
    lookup_field = "journalist_id"


class SubscriberAgeList(generics.ListCreateAPIView):
    queryset = Age.objects.all()
    serializer_class = PressSubscriberAgeSerializer
    pagination_class = PostPageNumberPagination


class SubscriberAgeDetail(generics.ListAPIView):
    queryset = Age.objects.all()
    serializer_class = PressSubscriberAgeSerializer
    pagination_class = PostPageNumberPagination

    def get_queryset(self):
        journalist_id = self.kwargs["journalist_id"]
        queryset = Age.objects.filter(journalist_id=journalist_id)
        return queryset


class SubscribersAgeByPressNameView(generics.ListAPIView):
    serializer_class = PressSubscriberAgeSerializer
    pagination_class = PostPageNumberPagination

    def get_queryset(self):
        press_name = self.kwargs["press_name"]  # URL에서 press_name을 가져옴
        queryset = Age.objects.filter(journalist__press__press_name=press_name)
        return queryset


class AgeRankingByCategoryView(generics.ListAPIView):
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
            press_ranking = press_ranking[:10]
            result.append({"age_group": age_group, "press_ranking": press_ranking})

        return result

    def get_age_subscriber_count(self, press, age_range):
        # Calculate the age-based subscriber count for the given press and age range
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


# class AgeRankingByCategoryView(APIView):
#     paginatoin_class = PostPageNumberPagination

#     def get(self, request):
#         age_ranges = [10, 20, 30, 40, 50, 60]
#         result = []

#         for age_range in age_ranges:
#             age_group = f"{age_range}대"
#             age_ranking = []

#             for category in Category.objects.all():
#                 category_name = category.category_name
#                 category_press_ranking = (
#                     Press.objects.annotate(
#                         age_subscriber_count=Coalesce(
#                             Sum(
#                                 Case(
#                                     When(
#                                         journalist__age__age=age_range,
#                                         then=F("journalist__subscriber_count")
#                                         * F("journalist__age__percentage")
#                                         / 100,
#                                     ),
#                                     default=Value(0),
#                                     output_field=models.IntegerField(),
#                                 )
#                             ),
#                             Value(0),
#                         )
#                     )
#                     .filter(category=category)
#                     .order_by("-age_subscriber_count")[:5]
#                 )

#                 category_ranking = {
#                     "category_name": category_name,
#                     "press_ranking": [
#                         {
#                             "press_name": press.press_name,
#                             "count": press.age_subscriber_count,
#                         }
#                         for press in category_press_ranking
#                     ],
#                 }

#                 age_ranking.append(category_ranking)

#             age_group_ranking = {"age_group": age_group, "categories": age_ranking}

#             result.append(age_group_ranking)

#         return Response(result)


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
