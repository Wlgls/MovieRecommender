from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Items'
urlpatterns = [
   
    path("", views.index, name='index'),
    path("mylist/", views.mylist, name='mylist'),
    path("recommend/", views.recommend, name='recommend'),
    path("add/", views.add, name='add')
]
