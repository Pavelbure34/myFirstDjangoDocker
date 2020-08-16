from django.db import models
from uuid import uuid4

# Create your models here.
class Reply(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # target_article = models.CharField(blank=False, null=False, max_length=256)
    author = models.CharField(blank=False, null=False, max_length=256)
    posted_DateTime = models.DateTimeField()
    contents = models.TextField()
    target_article = models.ForeignKey(
        'article.Article', related_name="unique_id_article", on_delete=models.CASCADE
    )

