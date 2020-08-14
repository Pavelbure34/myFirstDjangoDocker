from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # list_display = ['title, author']
    # ordering = ['title']
    # actions = []

    class Meta:
        model = Article

admin.site.register(Article, ArticleAdmin)
