'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True


DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

