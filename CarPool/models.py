from django.db import models

# Create your models here.

class CarPool(models.Model):
    title=models.CharField(max_length=200)
    writer= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

   