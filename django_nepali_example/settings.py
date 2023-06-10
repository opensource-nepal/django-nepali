"""
This file is a django settings file dedicated for
testing purposes

NOTE: keep it minimal
"""

DEBUG = True

INSTALLED_APPS = ("django_nepali",)

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
