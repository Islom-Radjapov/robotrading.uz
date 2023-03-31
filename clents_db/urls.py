from django.contrib import admin
from django.urls import path

from clents_db.views import my_view

urlpatterns = [
    path('', my_view)
]
