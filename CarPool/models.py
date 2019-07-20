from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CarPool(models.Model):
    title=models.CharField(max_length=200)
    writer= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    writer = models.CharField(max_length = 200)
    content = models.TextField()
    post = models.ForeignKey(CarPool, on_delete=models.CASCADE)
   