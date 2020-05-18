from django.db import models

# Create your models here.
# Base = declarative_base()


class Users(models.Model):
    class Meta:
        db_table = 'Users'
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100, unique=True, blank=False)
    Password = models.CharField(max_length=100, blank=False)


# engine = create_engine('mysql+mysqlconnector://smith:smith@127.0.0.1:3306/MovieRecommend')
# Base.metadata.create_all(engine)

