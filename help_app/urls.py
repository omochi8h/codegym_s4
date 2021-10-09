from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'help_app'
urlpatterns = [
    #path("", views.IndexView.as_view(), name="index"),
    #path("about/", views.AboutView.as_view(), name="about"),
]
