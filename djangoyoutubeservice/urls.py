from django.contrib import admin
from django.urls import path

from search.views import VideoListAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("videos/", VideoListAPIView.as_view(), name="video_search"),
]
