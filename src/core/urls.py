"""Core URL Configuration for flowreader."""

from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/admin"), name="index-redirect"),
    path("admin/", admin.site.urls),
]
