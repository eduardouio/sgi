"""
Django settings for sgi project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sj-z02b^$ifmzup+&qb+6!fi4mgbah_n3ddss@9m4=e0u$fdrr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]

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
    'authentication',
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


DATOS_EMPRESAS = {
    'cordovez' : {
        'nombre' : 'AGENCIAS Y REPRESENTACIONES CORDOVEZ S.A.',
        'empresa' : 'cordovez',
        'ruc' : '1790023516001',
        'direccion': 'AV. 10 DE AGOSTO N.57-186 Y LEONARDO MURIALDO ',
        'telefono': '022405911',
        'email' : 'sgi@cordovez.com.ec',
        'url_logo' : 'http://179.49.60.158:8888/img/logo_cordovez.jpg',
        'url_app' : 'http://179.49.60.158:5001/',
        'url_app_local' : 'http://192.168.0.198:5001/',
        'admin_title' : 'A&R Cordovez S.A.',
        'database' : 'cordovezApp',
    },
    'test' : {
        'nombre' : 'AMBIENTE DE PRUEBAS TEST',
        'empresa' : 'test',
        'ruc' : '1722919725001',
        'direccion': 'AV COLO 1133 Y AMAZONAS EDF ARISTA OF 500 ',
        'telefono': '022405911',
        'email' : 'sgi@cordovez.com.ec',
        'url_logo' : 'http://179.49.60.158:8888/img/logo_test.png',
        'url_app' : 'http://localhost:8000/',
        'url_app_local' : 'http://localhost:8000/',
        'admin_title' : 'TEST',
        'database' : 'cordovezAppTEST',
    },
    'imnac' : {
        'nombre' : 'IMNAC IMPORTADORA NACIONAL CIA LTDA',
        'empresa' : 'imnac',
        'ruc' : '1792324289001',
        'direccion': 'LA PAZ PAUL RIVET 227 Y JAMES ORTON ',
        'telefono': '022405911',
        'email' : 'sgi@imnac.com.ec',
        'url_logo' : 'http://179.49.60.158:8888/img/logo_imnac.jpg',
        'url_app' : 'http://179.49.60.158:5002/',
        'url_app_local' : 'http://192.168.0.198:5002/',
        'admin_title' : 'IMNAC CIA LTDA',
        'database' : 'imnacApp',
    },
    'vid' : {
        'nombre' : 'VIDINTERNACIONAL S.A.',
        'empresa' : 'vid',
        'ruc' : '1791771907001',
        'direccion': 'AV. 10 DE AGOSTO N.57-186 Y LEONARDO MURIALDO ',
        'telefono': '022405911',
        'email' : 'sgi@vidinternacional.com.ec',
        'url_logo' : 'http://179.49.60.158:8888/img/logo_vid.jpg',
        'url_app' : 'http://179.49.60.158:5003/',
        'url_app_local' : 'http://192.168.0.198:5003/',
        'admin_title' : 'VIDINTERNACIONAL S.A.',
        'database' : 'vidApp',

    },
}

#Seleccionamos la empresa
EMPRESA = DATOS_EMPRESAS['cordovez']
GRAPPELLI_ADMIN_TITLE = EMPRESA['admin_title']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': EMPRESA['database'],
        'USER' : 'appCordovez',
        'PASSWORD' : '\DBGfW<7;vBa5(LB',
        'HOST': '179.49.60.158',
        'PORT' : '3306',
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

USE_TZ = True

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', 'guardian.backends.ObjectPermissionBackend')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['static_django'])

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['static']),
]

STATIC_URL = '/static/'


MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['media'])
MEDIA_URL = '/media/'
