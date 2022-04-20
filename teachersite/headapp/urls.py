from django.urls import path

from headapp.views import *

urlpatterns = [
    path('', index),
    path('about/', about),
]