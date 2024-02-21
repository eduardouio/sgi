"""
Django settings for sgi project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from .enterprise_data import EMPRESA, CMT_DEBUG

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = EMPRESA['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simple_history',
    'guardian',
    'rest_framework',
    'import_export',
    'django_extensions',
    'authentication',
    'numpy',
    'api',
    'filemanager',
    'costings',
    'suppliers',
    'orders',
    'paids',
    'partials',
    'migrationSAP',
    'products',
    'warenhouse',
    'importations',
    'audit',
    'reports',
    'almagro',
    'labels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'sgi.middleware.DataCompletionMiddleware',
]

ROOT_URLCONF = 'sgi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': '',
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
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': ['templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'jinja2_bridge.environment',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

WSGI_APPLICATION = 'sgi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Seleccionamos la empresa
GRAPPELLI_ADMIN_TITE = EMPRESA['admin_title']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': EMPRESA['database'],
        'USER': EMPRESA['db_user'],
        'PASSWORD': EMPRESA['db_passwd'],
        'HOST': EMPRESA['db_host'],
        'PORT': EMPRESA['db_port'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = False

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'guardian.backends.ObjectPermissionBackend')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.sep.join(os.path.abspath(
    __file__).split(os.sep)[:-2]+['static_django'])

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['static']),
]

STATIC_URL = '/static/'


MEDIA_ROOT = os.sep.join(os.path.abspath(
    __file__).split(os.sep)[:-2]+['media'])
MEDIA_URL = '/media/'

LOGIN_URL = '/login/'