from django.db import models

# Create your models here.
class LostAndFound(models.Model) :
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length = 200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')

    def __str__(self) :
        return self.title

    def summary(self) :
        return self.body[:100]

class Comment(models.Model) :
    lost = models.ForeignKey(LostAndFound, on_delete = models.CASCADE, related_name = "comments")
    comment_created = models.DateField('date published')
    comment_writer = models.CharField(max_length = 200)
    comment_text = models.TextField()

    def __str__(self) :
        return self.comment_writer + "의 댓글"