from django.urls import path
from . import views
from press.views import AgePressRanking


app_name = "press"

urlpatterns = [
    # path('', views.display_age_press_ranking, name='press-ranking'),
    # path('category/<str:category>/', views.category_view, name='category'),
    # path('', views.display_age_press_ranking, name='press-ranking'),
    # path('category/<str:category>/', views.category_view, name='category-view'),
]