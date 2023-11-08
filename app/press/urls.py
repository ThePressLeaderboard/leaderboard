from django.urls import path

app_name = "press"


urlpatterns = [
    path("api/press",),
    path("api/press/<int:pk>/"),
    path("api/press/<int:pk/journalist"),
    path("api/press/<int:pk/age"),
    path("api/press/<int:pk/ranking/journalist"),
    path("api/press/ranking/subscribers"),
    path("api/press/ranking/age"),
    path("api/press/ranking/gender"),
    path("api/press/ranking/cheer"),
    path("api/journalist"),
    path("api/journalist/<int:pk"),
    path("api/journalist/<int:pk/subscribersgender"),
    path("api/journalist/<int:pk/subscribersage"),
    path("api/journalist/<int:pk/section"),
    path("api/section"),
    path("api/category"),
]
