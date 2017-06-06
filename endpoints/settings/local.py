"""Development settings and globals."""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *

DEBUG = True

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': join(SITE_ROOT, 'db.local'),
#    }
#}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
    }
}
