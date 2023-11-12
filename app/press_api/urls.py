from django.urls import path
from .views import (
    AgeRankingByCategoryView,
    CategoryList,
    CategoryDetail,
    PressList,
    PressDetail,
    JournalistList,
    JournalistDetail,
    SubscriberAgeList,
    SubscriberAgeDetail,
    TotalAgeByPress,
)


urlpatterns = [
    path("api/press/category/", CategoryList.as_view(), name="category-list"),
    path(
        "api/press/category/<int:pk>/", CategoryDetail.as_view(), name="category-detail"
    ),
    path("api/press/press/", PressList.as_view(), name="press-list"),
    path("api/press/press/<int:pk>/", PressDetail.as_view(), name="press-detail"),
    path("api/press/journalist/", JournalistList.as_view(), name="journalists-list"),
    path(
        "api/press/journalist/<int:journalist_id>/",
        JournalistDetail.as_view(),
        name="journalist-detail",
    ),
    path(
        "api/press/journalist/<int:journalist_id>/subscriberage",
        SubscriberAgeDetail.as_view(),
        name="subscribers-age-detail",
    ),
    path(
        "api/press/press/ranking/age",
        AgeRankingByCategoryView.as_view(),
        name="press-ranking-by-age",
    ),
    path(
        "api/press/press/<str:press_name>/age/",
        TotalAgeByPress.as_view(),
        name="age-distribution-by-press-name",
    ),
]
