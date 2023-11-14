from django.urls import path
from .views import (
    SubscriberAgeDetail,
    TotalAgeByPress,
    AgePressRanking,
    CategoryWiseAgePressRanking,
    CategoryDetail,
    CategoryJournalistRanking,
    CategoryPressRanking,
    CategoryRanking,
    JournalistDetail,
    JournalistRanking,
    PressDetail,
    PressJournallistRanking,
    PressRanking,
    SectionDetail,
    SectionJournallistRanking,
    SectionRanking,
)


urlpatterns = [
    path("category/", CategoryRanking.as_view(), name="categoryranking"),
    path(
        "category/<str:category_name>/", CategoryDetail.as_view(), name="categorydetail"
    ),
    path(
        "category/<str:category_name>/press/",
        CategoryPressRanking.as_view(),
        name="categorypressranking",
    ),
    path(
        "category/<str:category_name>/journalist/",
        CategoryJournalistRanking.as_view(),
        name="categoryjournliastranking",
    ),
    path("press", PressRanking.as_view(), name="pressranking"),
    path("press/<str:press_name>/", PressDetail.as_view(), name="pressdetail"),
    path(
        "press/<str:press_name>/journalist/",
        PressJournallistRanking.as_view(),
        name="pressjournalistranking",
    ),
    path("section/", SectionRanking.as_view(), name="sectionranking"),
    path("section/<str:section_name>/", SectionDetail.as_view(), name="sectiondetail"),
    path(
        "section/<str:section_name>/journalist/",
        SectionJournallistRanking.as_view(),
        name="setionjournalistranking",
    ),
    path("journalist/", JournalistRanking.as_view(), name="journalistranking"),
    path(
        "journalist/<int:journalist_id>/",
        JournalistDetail.as_view(),
        name="journalistdetail",
    ),
    path(
        "journalist/<int:journalist_id>/subscriberage/",
        SubscriberAgeDetail.as_view(),
        name="subscribers-age-detail",
    ),
    path(
        "press/ranking/categoryage/",
        AgePressRanking.as_view(),
        name="press-ranking-by-categoryage",
    ),
    path(
        "press/ranking/onlyage",
        CategoryWiseAgePressRanking.as_view(),
        name="press-ranking-by-age",
    ),
    path(
        "press/<str:press_name>/age/",
        TotalAgeByPress.as_view(),
        name="age-distribution-by-press-name",
    ),
]
