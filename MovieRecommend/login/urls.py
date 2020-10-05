#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/05/13 20:24
@Author  : 彭友
@Version  : 设计了登录页面的主要urls
@File    : urls.py
@Software: PyCharm
@Contact : peeeyiii@163.com
"""


from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path("", views.login, name='login'),
    path("register", views.register, name='register'),
    path('quit', views.quit, name='quit'),
    path("logout", views.logout, name='logout'),
]
