from django.db import models

# Create your models here.
class Movies(models.Model):
    MovieTitle = models.CharField('电影名称',max_length = 100)
    Cover = models.ImageField('链接',upload_to='')
    StoryLine = models.TextField('电影简介',null = True, blank = True)

    def __str__(self):
        return self.MovieTitle
