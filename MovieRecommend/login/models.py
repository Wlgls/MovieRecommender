from django.db import models
class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=128, unique=True)
    Password = models.CharField(max_length=256)

    class Meta:
        db_table = 'Users'
        ordering = ['UserID']
