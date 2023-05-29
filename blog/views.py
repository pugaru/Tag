from django.conf import settings
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from tagging.models import Tag
from tagging.utils import LOGARITHMIC
from tagging.views import TaggedObjectList

from .models import Page, ImagePost, ImageCategory


def generate_tag_cloud(nolimit=False):
    cloud = Tag.objects.cloud_for_model(
        ImagePost,
        steps=9,
        distribution=LOGARITHMIC,
        filters=None,
        min_count=None)
    if not nolimit:
        limit = settings.TAG_CLOUD_LIMIT
        if len(cloud) > limit:
            while len(cloud) > limit:
                min_value = min(tag.count for tag in cloud)
                min_tag = [tag for tag in cloud if tag.count == min_value][0]
                cloud.remove(min_tag)
    return cloud


def generate_related_tags(tag):
    tags = Tag.objects.related_for_model(
        tag,
        ImagePost,
        counts=True,
        min_count=None)
    limit = settings.RELATED_TAGS_LIMIT
    if len(tags) > limit:
        while len(tags) > limit:
            min_value = min(tag.count for tag in tags)
            min_tag = [tag for tag in tags if tag.count == min_value][0]
            tags.remove(min_tag)
    return tags


class HomepageView(ListView):
    model = ImagePost
    context_object_name = 'photos'
    paginate_by = 10

    def get_queryset(self):
        queryset = ImagePost.objects.filter(category__exclude_from_homepage=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'homepage-view'
        if settings.SEO_BLOG_TITLE:
            context['page_title'] = settings.SEO_BLOG_TITLE
        else:
            context['page_title'] = settings.BLOG_NAME
        if settings.SEO_BLOG_DESCRIPTION:
            context['page_description'] = settings.SEO_BLOG_DESCRIPTION
        elif settings.BLOG_DESCRIPTION:
            context['page_description'] = settings.BLOG_DESCRIPTION
        context['featured_pages'] = Page.objects.filter(homepage_featured=True)
        context['all_photos'] = ImagePost.objects.filter(category__exclude_from_homepage=False)
        context['tag_cloud'] = generate_tag_cloud()
        return context


class PhotoView(DetailView):
    model = ImagePost
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'photo-detail'
        context['page_title'] = self.object.title
        if self.object.description:
            context['page_description'] = self.object.description
        return context


class TagView(TaggedObjectList):
    model = ImagePost
    context_object_name = 'photos'
    paginate_by = 10
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'tag-view'
        context['page_title'] = '#{} photos'.format(self.tag)
        context['all_photos'] = ImagePost.objects.all()
        context['page_description'] = 'Photos tagged with #{}'.format(self.tag)
        context['tag_cloud'] = generate_tag_cloud()
        context['related_tags'] = generate_related_tags(self.tag)
        return context


class CategoryView(ListView):
    model = ImagePost
    context_object_name = 'photos'
    paginate_by = 10
    allow_empty = True

    def get_queryset(self):
        queryset = ImagePost.objects.filter(category__slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ImageCategory.objects.get(slug=self.kwargs['slug'])
        context['view'] = 'category-view'
        context['page_title'] = '{}'.format(context['category'])
        context['all_photos'] = ImagePost.objects.filter(category__slug=self.kwargs['slug'])
        context['page_description'] = '{}'.format(context['category'])
        context['tag_cloud'] = generate_tag_cloud()
        return context

class PageView(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'page-view'
        page = self.object
        if page.seo_title:
            context['page_title'] = page.seo_title
        else:
            context['page_title'] = page.title
        if page.seo_description:
            context['page_description'] = page.seo_description
        if page.page_head:
            context['page_head'] = page.page_head
        if page.page_styles:
            context['page_styles'] = page.page_styles
        return context


def tag_list(request):
    tag_cloud = generate_tag_cloud(nolimit=True)
    template = 'blog/tag_list.html'
    context = {
        'page_title': 'Tags',
        'tag_cloud': tag_cloud}
    return render(request, template, context)
