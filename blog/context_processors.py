from django.conf import settings

from .models import Page, ImageCategory


def config_processor(request):
    config = {
       'BLOG_NAME': settings.BLOG_NAME,
       'BLOG_DESCRIPTION': settings.BLOG_DESCRIPTION,
       'CONTACT_PAGE_TITLE': settings.CONTACT_PAGE_TITLE,
       'SEO_NOINDEX': settings.SEO_NOINDEX,
       'SOCIAL_PROFILES': settings.SOCIAL_PROFILES,
       'FACEBOOK_URL': settings.FACEBOOK_URL,
       'INSTAGRAM_URL': settings.INSTAGRAM_URL,
    }
    return {'config': config}


def nav_processor(request):
    return {
        'nav_items': Page.objects.filter(show_in_menu=True),
        'image_categories': ImageCategory.objects.filter(show_in_menu=True)
    }
