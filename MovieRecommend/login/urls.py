
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login),
    # 在path里表示网页地址时根目录为"",但是注意在redirect中表示时为"/"
    path("login/register", views.register),
    path("login/index", views.index),
    path("login/index/logout", views.confirm_out),
    path("login/logout", views.logout)
]
