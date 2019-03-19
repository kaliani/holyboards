
from django.contrib import admin
from django.urls import path
from boards.views import index
from django.conf.urls import url

urlpatterns = [
    url(r'^', index),
]
