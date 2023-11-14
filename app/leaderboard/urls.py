from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("press/", include("press.urls")),
    path("press_api/", include("press_api.urls")),
]
