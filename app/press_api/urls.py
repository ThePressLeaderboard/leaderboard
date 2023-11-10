from django.urls import path
from .views import *


urlpatterns = [
    path('category', CategoryList.as_view(), name='categorylise'),
    path('category/<str:category_name>', CategoryDetail.as_view(), name='categorydetail'),
    path('category/<str:category_name>/press', CategoryPress.as_view(), name='categorypress'),
    path('category/<str:category_name>/journalist', CategoryJournalist.as_view(), name='categoryjournalist'),
    path('press', PressList.as_view(), name='presslist'),
    path('press/<str:name>', PressDetail.as_view(), name='pressdetail'),
    path('press/<str:press_name>/journalist', PressJournallist.as_view(), name='pressjournalist'),
    path('ranking/press', PressRanking.as_view(), name='pressranking'),
    path('ranking/category', CategoryRanking.as_view(), name='categoryranking'),
    path('ranking/category/<str:category_name>/press', CategoryPressRanking.as_view(), name='categorypressranking'),
    path('ranking/category/<str:category_name>/journalist', CategoryJournalistRanking.as_view(), name='categoryjournliastranking'),
    path('ranking/press/<str:press_name>/journalist', PressJournallistRanking.as_view(), name='pressjournalistranking'),
    path('ranking/journalist', JournalistRanking.as_view(), name='journalistranking'),
]