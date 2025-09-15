"""
Django settings for oc_lettings_site project.

This module contains all the configuration for the Django project, including:
- Paths
- environment variables
- Security settings
- Installed applications
- Middleware
- Templates
- Database
- Authentication
- Internationalization
- Static files

For more information, see:
https://docs.djangoproject.com/en/3.0/topics/settings/
"""


import logging
import os
from pathlib import Path

import sentry_sdk
from django.core.management.utils import get_random_secret_key
from environs import env
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.django import DjangoIntegration

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# environment variables
# -------------------------------------------------------------------

env.read_env()
DEBUG = env.bool("DEBUG", True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# -------------------------------------------------------------------
# Security
# -------------------------------------------------------------------


# SECURITY WARNING: keep the secret key used in production secret!
# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env.str("OC_LETTINGS_SECRET_KEY", default=get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
OSTS = ['localhost',
                 '127.0.0.1',
                 'p13-python-oc-lettings-fr.onrender.com']

# -------------------------------------------------------------------
# Application definition
# -------------------------------------------------------------------

INSTALLED_APPS = [
    'oc_lettings_site.apps.OCLettingsSiteConfig',  # Main project app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'lettings',
    'profiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

# -------------------------------------------------------------------
# Templates
# -------------------------------------------------------------------

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
            ],
        },
    },
]

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'


# -------------------------------------------------------------------
# Database
# -------------------------------------------------------------------

# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# -------------------------------------------------------------------
# Password validation
# -------------------------------------------------------------------

# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# -------------------------------------------------------------------
# Internationalization
# -------------------------------------------------------------------

# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -------------------------------------------------------------------
# Static files
# -------------------------------------------------------------------

# https://docs.djangoproject.com/en/3.0/howto/static-files/

# URL to serve static files
STATIC_URL = '/static/'

# Directories with static files for development
STATICFILES_DIRS = [BASE_DIR / "static"]

# Directory where static files are collected in production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------------------------------------------------------
# Sentry logging
# -------------------------------------------------------------------

sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR
)

sentry_sdk.init(
    dsn=env.str("SENTRY_DSN_OC_LETTINGS", default=""),
    integrations=[DjangoIntegration(), sentry_logging],
    traces_sample_rate=1.0,
    send_default_pii=True,
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "sentry": {
            "level": "INFO",
            "class": "sentry_sdk.integrations.logging.EventHandler",
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["sentry", "console"],
    },
    "loggers": {
        "django": {
            "level": "INFO",
            "handlers": ["sentry", "console"],
            "propagate": False,
        },
        "django.request": {
            "level": "INFO",
            "handlers": ["sentry", "console"],
            "propagate": False,
        },
        "django.security": {
            "level": "ERROR",
            "handlers": ["sentry", "console"],
            "propagate": False,
        },
        "lettings": {
            "level": "INFO",
            "handlers": ["sentry", "console"],
            "propagate": False,
        },
        "profiles": {
            "level": "INFO",
            "handlers": ["sentry", "console"],
            "propagate": False,
        },
        "oc_lettings_site": {
            "level": "INFO",
            "handlers": ["sentry", "console"],
            "propagate": False,
        },
    },
}
