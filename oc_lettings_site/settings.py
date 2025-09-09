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
from environs import env
import os

from pathlib import Path

import sentry_sdk
from django.core.management.utils import get_random_secret_key

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# environment variables
# -------------------------------------------------------------------

env.read_env()

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
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1']

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

sentry_sdk.init(
    dsn=env("SENTRY_DSN_OC_LETTINGS"),
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "sentry": {
            "level": "INFO",
            "class": "logging.NullHandler",
        },
    },
    "root": {
        "level": "ERROR",
        "handlers": ["sentry"],
    },
    "loggers": {
        "django.request": {
            "level": "INFO",
            "handlers": ["sentry"],
            "propagate": False,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["sentry"],
            "propagate": False,
        },
    },
}
