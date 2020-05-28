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


class Ratings(models.Model):
    class Meta:
        db_table = 'Rating'
    
    ID = models.AutoField(primary_key=True)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    Movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
