from .base import *


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'dotme',
        'USER': 'dotme',
        'PASSWORD': 'dotme',
    }
}

