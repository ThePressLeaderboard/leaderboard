from django.urls import path
from .views import *


urlpatterns = [
    path('press', PressList.as_view(), name='presslist'),
    path('press/<str:name>', PressDetail.as_view(), name='pressdetail'),
    path('press/<str:press_name>/journalist', PressJournallist.as_view(), name='pressjournalist'),
    path('ranking/press', PressRanking.as_view(), name='pressranking'),
    path('ranking/press/<str:press_name>/journalist', PressJournallistRanking.as_view(), name='pressjournalistranking'),
    path('ranking/journalist', JournalistRanking.as_view(), name='journalistranking'),
]