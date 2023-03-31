from django.contrib import admin
from django.urls import path

from base1.views import my_view

urlpatterns = [
    path('', my_view)
]
