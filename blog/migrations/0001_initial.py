# Generated by Django 3.2.5 on 2021-07-03 10:28

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import easy_thumbnails.fields
import tagging.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('show_in_menu', models.BooleanField(default=True)),
                ('menu_position', models.IntegerField(default=0)),
                ('exclude_from_homepage', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('menu_position',),
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('show_in_menu', models.BooleanField(default=True)),
                ('menu_position', models.IntegerField(default=0)),
                ('homepage_featured', models.BooleanField(default=False)),
                ('featured_image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='')),
                ('seo_title', models.CharField(blank=True, max_length=200, null=True)),
                ('seo_description', models.CharField(blank=True, max_length=200, null=True)),
                ('seo_noindex', models.BooleanField(default=False)),
                ('page_head', models.TextField(blank=True, null=True)),
                ('page_styles', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('menu_position',),
            },
        ),
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='published date')),
                ('title', models.CharField(max_length=200)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='')),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('tags', tagging.fields.TagField(blank=True, max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.imagecategory')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]