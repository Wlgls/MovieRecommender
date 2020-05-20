from django.urls import path
from django.conf.urls import url
from Items import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
]
