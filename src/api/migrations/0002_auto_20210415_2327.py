# Generated by Django 3.1.7 on 2021-04-15 17:57

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='participants',
        ),
        migrations.AddField(
            model_name='podcast',
            name='participants',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
