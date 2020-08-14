from django.db import models

# Create your models here.
class Reply(models.Model):
    target_article = models.CharField(blank=False, null=False, max_length=256)
    author = models.CharField(blank=False, null=False, max_length=256)
    posted_DateTime = models.DateTimeField()
    contents = models.TextField()
