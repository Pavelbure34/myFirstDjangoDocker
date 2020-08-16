from django.contrib import admin
from .models import Reply

# Register your models here.
class ReplyAdmin(admin.ModelAdmin):
    class Meta:
        model = Reply

admin.site.register(Reply, ReplyAdmin)
