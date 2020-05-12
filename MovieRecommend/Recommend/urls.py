from django.urls import path
from Recommend import views

urlpatterns = [
    path("", views.index),
]