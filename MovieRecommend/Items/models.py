# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2020/06/15 19:12:46
@Author  :   王强和张聪
@Version :   1.0： 建立了电影的数据库（张聪）
@Version :   1.1:  建立了Ratings和Recommend的数据库（王强）
@Contact :   smithguazi@gmail.com
'''

from django.db import models
from login.models import Users
# Create your models here.
class Movies(models.Model):
    class Meta:
        db_table = 'Movies'
    
    MovieID = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=100, blank=False)
    Cover = models.CharField(max_length=100)
    StoryLine = models.TextField(max_length=1000)
    DoubanLink = models.CharField(max_length=100)
    grade = models.IntegerField()

class Ratings(models.Model):
    class Meta:
        db_table = 'Ratings'
    
    ID = models.AutoField(primary_key=True)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

class Recommend(models.Model):
    class Meta:
        db_table = 'Recommend'

    ID = models.AutoField(primary_key=True)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    kind = models.CharField(max_length=20, default='user')