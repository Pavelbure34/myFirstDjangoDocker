# Generated by Django 3.0.7 on 2020-08-14 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='targetArticle',
            new_name='target_article',
        ),
    ]
