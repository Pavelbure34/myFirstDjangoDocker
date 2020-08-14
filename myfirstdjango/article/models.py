from django.db import models

# Create your models here.
class Article(models.Model):
    end_point = models.CharField(blank=False, null=False, max_length=256)
    title = models.CharField(blank=False, null=False, max_length=256)
    author = models.CharField(blank=False, null=False, max_length=256)
    posted_DateTime = models.DateTimeField()
    likes = models.IntegerField(default=1, blank=True, null=True)
    contents = models.TextField()
     