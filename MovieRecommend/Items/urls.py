from django.urls import path
from Items import views

urlpatterns = [
    path('', views.index),
]