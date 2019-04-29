# Generated by Django 2.2 on 2019-04-29 14:52

import ckeditor.fields
from django.db import migrations, models
import django_extensions.db.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='title')),
                ('post_date', models.DateField(auto_now_add=True)),
                ('post_update', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('short_desc', models.TextField(max_length=250)),
                ('status', models.BooleanField(default=False, verbose_name='Approve Post')),
                ('body', ckeditor.fields.RichTextField()),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
