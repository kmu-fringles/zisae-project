from django.db import models

# Create your models here.
class LostAndFound(models.Model) :
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length = 200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self) :
        return self.title

    def summary(self) :
        return self.body[:100]