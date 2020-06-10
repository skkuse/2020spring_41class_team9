"""
Django settings for MODU project.

Based on by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from django.core.exceptions import ImproperlyConfigured
import json
import os
import posixpath

def get_json_from(json, setting):
    try:
        return json[setting]
    except KeyError:
        error_msg = "Error occured while loading {}.json.".format(json)
        raise ImproperlyConfigured(error_msg)

if os.getenv('MODU_PRODUCTION') != None:
    MODU_PRODUCTION = True
    print('Production mode activated.')
    print(os.getenv('MODU_PRODUCTION'))
else:
    MODU_PRODUCTION = False


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if MODU_PRODUCTION:
    SECRET_KEY = os.getenv('MODU_SECRET_KEY')
    assert SECRET_KEY != 'None'
else:
    with open(os.path.join(BASE_DIR, 'settings/secrets.json')) as f:
        secrets = json.loads(f.read())
    SECRET_KEY = get_json_from(secrets, 'DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not MODU_PRODUCTION

if os.getenv('ALLOWED_HOSTS') != None:
    ALLOWED_HOSTS = [ os.getenv('ALLOWED_HOST') ]
else:
    ALLOWED_HOSTS = []


# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authentication.apps.AuthenticationConfig',
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MODU.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
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

WSGI_APPLICATION = 'MODU.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
database_filename = (os.path.join(BASE_DIR, 'settings/database.json'))

if MODU_PRODUCTION:
    MODU_DB_NAME = os.getenv('MARIADB_DBNAME')
    MODU_DB_USER = os.getenv('MARIADB_USERNAME')
    MODU_DB_PASSWORD = os.getenv('MARIADB_PW')
    MODU_DB_HOST = os.getenv('MARIADB_HOST')
    MODU_DB_PORT = os.getenv('MARIADB_PORT')
    assert MODU_DB_NAME != 'None'
    assert MODU_DB_USER != 'None'
    assert MODU_DB_PASSWORD != 'None'
    assert MODU_DB_HOST != 'None'
    assert MODU_DB_PORT != 'None'
else:
    with open(database_filename) as file:
        db_settings = json.loads(file.read())
    MODU_DB_NAME = get_json_from(db_settings, 'MARIADB_DBNAME')
    MODU_DB_USER = get_json_from(db_settings, 'MARIADB_USERNAME')
    MODU_DB_PASSWORD = get_json_from(db_settings, 'MARIADB_PW')
    MODU_DB_HOST = get_json_from(db_settings, 'MARIADB_HOST')
    MODU_DB_PORT = get_json_from(db_settings, 'MARIADB_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MODU_DB_NAME,
        'USER': MODU_DB_USER,
        'PASSWORD': MODU_DB_PASSWORD,
        'HOST': MODU_DB_HOST,
        'PORT': MODU_DB_PORT,
    }
}

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
LOGOUT_REDIRECT_URL = '/'
AUTHENTICATION_BACKENDS  = ['authentication.FirebaseRESTBackend']
AUTH_USER_MODEL = 'model.Developer'

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
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Firebase REST API setting
if MODU_PRODUCTION:
    FIREBASE_API_KEY = os.getenv('FIREBASE_API_KEY')
    assert FIREBASE_API_KEY != 'None'
else:
    with open(os.path.join(BASE_DIR, 'settings/secrets.json')) as f:
        secrets = json.loads(f.read())
    FIREBASE_API_KEY = get_json_from(secrets, 'FIREBASE_API_KEY')
