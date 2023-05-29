from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField
from tagging.fields import TagField


class ImagePost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField('published date',default=timezone.now,blank=True)
    title = models.CharField(max_length=200)
    image = ThumbnailerImageField()
    description = models.TextField(blank=True, null=True, max_length=200)
    tags = TagField()
    category = models.ForeignKey('ImageCategory', null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)


class ImageCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    show_in_menu = models.BooleanField(default=True)
    menu_position = models.IntegerField(default=0)
    exclude_from_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('menu_position',)


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField(blank=True, null=True)
    show_in_menu = models.BooleanField(default=True)
    menu_position = models.IntegerField(default=0)
    homepage_featured = models.BooleanField(default=False)
    featured_image = ThumbnailerImageField(blank=True, null=True)
    seo_title = models.CharField(max_length=200, blank=True, null=True)
    seo_description = models.CharField(max_length=200, blank=True, null=True)
    seo_noindex = models.BooleanField(default=False)
    page_head = models.TextField(blank=True, null=True)
    page_styles = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('menu_position',)
