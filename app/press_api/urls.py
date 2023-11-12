from django.urls import path

from .views import FemalePressRanking, JournalistGenderDetail, MalePressRanking

urlpatterns = [
    path("press/ranking/male", MalePressRanking.as_view(), name="male-press-ranking"),
    path(
        "press/ranking/female",
        FemalePressRanking.as_view(),
        name="female-press-ranking",
    ),
    path(
        "journalist/<int:pk>/gender",
        JournalistGenderDetail.as_view(),
        name="journalist-gender-detail",
    ),
]
