from django.db import models
from uuid import uuid4

# Create your models here.
class Article(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    end_point = models.CharField(blank=False, null=False, max_length=256)
    title = models.CharField(blank=False, null=False, max_length=256)
    author = models.CharField(blank=False, null=False, max_length=256)
    posted_DateTime = models.DateTimeField()
    likes = models.IntegerField(default=1, blank=True, null=True)
    contents = models.TextField()
    replies = models.ForeignKey(
        'reply.Reply', related_name="target_article_reply", on_delete=models.CASCADE
    )