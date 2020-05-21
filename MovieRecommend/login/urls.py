from django.urls import path
from . import views

urlpatterns = [
    path("", views.login),
    path("register", views.register),
    path("index", views.index),
    path("index/logout", views.confirm_out),
    path("logout", views.logout)
]


