"""
Django settings for ImpactWebsite project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import configparser

from django.contrib.staticfiles import storage
from django.urls import reverse


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#CSRF_TRUSTED_ORIGINS = ['localhost:60']
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#9g@fst18g4q-&^+o9r-#q$3)d%%8@4kv4asgk&q#on+i0+yyg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True#bool(os.environ.get("DEBUG", default=Fa;se))

ALLOWED_HOSTS = []#os.environ.get("DJANGO_ALLOWED_HOSTS").split(':')

config = configparser.ConfigParser()
with open('ImpactWebsite/DATA.ini') as conf:
    config.read_file(conf)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'impact_website.apps.ImpactWebsiteConfig',
    'auth_system',
    'rest_framework.authtoken',
    'posting',
    #'bootstrap4',
    'api',
    'rest_framework',
    #'corsheaders',
]

#CORS_ORIGIN_ALLOW_ALL = True
#CORS_ORIGIN_WHITELIST = ['http://localhost:3001', 'http://localhost:3000']


MIDDLEWARE = [
    #'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
   # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ImpactWebsite.urls'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

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

WSGI_APPLICATION = 'ImpactWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

name = config.get('DATABASE', 'name')
username = config.get('DATABASE', 'username')
password = config.get('DATABASE', 'password')
use_postgre = config.get('DATABASE', 'use_postgre')

if use_postgre == 'True':
    DATABASES = {
        'default': {
            "ENGINE": os.environ.get("DJANGO_SQL_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": os.environ.get("SQL_USER", "impact_website"),
            "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
            "HOST": os.environ.get("SQL_HOST", "db"),
            "PORT": os.environ.get("SQL_PORT", "5432"),       
        }

    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_URL = '/static_served/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_served')
# Override default user
AUTH_USER_MODEL = 'auth_system.User'

# Production settings
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    STATIC_URL = '/static_served/'
    STATICFILES_STORAGE = storage.ManifestStaticFilesStorage
    CSRF_COOKIE_SECURE = True


