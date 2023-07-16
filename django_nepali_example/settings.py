"""
This file is a django settings file dedicated for
testing purposes

NOTE: keep it minimal
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

INSTALLED_APPS = ("django_nepali", "django_nepali_example")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            # ... some options here ...
        },
    },
]

USE_TZ = True
TIME_ZONE = "UTC"

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
