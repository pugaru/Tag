import os

import dj_database_url
from decouple import config


# Blog config

BLOG_NAME = config('BLOG_NAME', default='Photoblog')
BLOG_DESCRIPTION = config('BLOG_DESCRIPTION', default='Just try it')
CONTACT_FORM_EMAIL = config('CONTACT_FORM_EMAIL',default='Email')
CONTACT_PAGE_TITLE = config('CONTACT_PAGE_TITLE', default='Contact')
CONTACT_PAGE_SLUG = config('CONTACT_PAGE_SLUG', default='contact')
CONTACT_PAGE_DESCRIPTION = config(
    'CONTACT_PAGE_DESCRIPTION',
    default='Send me a message using the form below.')
TAG_CLOUD_LIMIT = config('TAG_CLOUD_LIMIT', default=10, cast=int)
RELATED_TAGS_LIMIT = config('RELATED_TAGS_LIMIT', default=5, cast=int)
SEO_BLOG_TITLE = config('SEO_BLOG_TITLE', default=None)
SEO_BLOG_DESCRIPTION = config('SEO_BLOG_DESCRIPTION', default=None)
SEO_NOINDEX = config('SEO_NOINDEX', default=False, cast=bool)
SOCIAL_PROFILES = config('SOCIAL_PROFILES', default=False, cast=bool)
FACEBOOK_URL = config('FACEBOOK_URL', default='https://github.com/mckdev/django-photoblog')
INSTAGRAM_URL = config('INSTAGRAM_URL', default='https://github.com/mckdev/django-photoblog')


# General config

ALLOWED_HOSTS = ['*']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True
SECRET_KEY = 'django-insecure-820p6)d30ijnq=^!sobqkl^)hdb-&sf2)f2h3!hjb0zbw2b%9='
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SITE_ID = 1


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
    }
}



# Email backend

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_USE_TLS = True
    EMAIL_HOST = config('EMAIL_HOST',default=None)
    EMAIL_HOST_USER = config('EMAIL_HOST_USER',default=None)
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD',default=None)
    EMAIL_PORT = 587


# App config

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'contact_form.apps.ContactFormConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'tagging',
    'ckeditor',
    'ckeditor_uploader',
    'widget_tweaks',
    'storages',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware'
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.nav_processor',
                'blog.context_processors.config_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static-root')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# S3 Media Storage

if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME',default=None)
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID',default=None)
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY',default=None)
    DEFAULT_FILE_STORAGE = 'website.storage_backends.MediaStorage'
    THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE  # easy_thumbnails
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    AWS_QUERYSTRING_AUTH = False


# Thumbnails

THUMBNAIL_ALIASES = {
    '': {
        'medium': {'size': (500, 500), 'crop': True},
        'carousel': {'size': (800, 800), 'crop': False},
    },
}


# CKEditor

CKEDITOR_UPLOAD_PATH = ""
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Maximize', 'Format', 'Bold', 'Italic', 'Underline', '-', 'TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor', 'Image', 'Embed', '-'],
            ['Undo', 'Redo', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo', 'Find', 'Replace', '-', 'SelectAll', '-', 'Source']
        ],
        'height': 400,
        'width': '100%',
        'extraPlugins': ','.join(
            [
                'image2',
                'embed',
            ]),
        'language': 'en',
    },

}
DEFAULT_AUTO_FIELD='django.db.models.AutoField'
