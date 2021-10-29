"""
Django settings for portfolioproject project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import psycopg2 as db
from psycopg2 import connect
import django_heroku
from django.contrib import staticfiles, postgres
import boto3
import base64
from storages.backends.s3boto3 import S3Boto3Storage
from botocore.exceptions import ClientError
import json
from django.core.exceptions import ImproperlyConfigured
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'Optional default value')

# with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
#    secrets = json.load(secrets_file)
#
#
# def get_secret(setting, secrets=secrets):
#    """Get secret setting or fail with ImproperlyConfigured"""
#    try:
#        return secrets[setting]
#    except KeyError:
#        raise ImproperlyConfigured("Set the {} setting".format(setting))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#DEBUG_PROPAGATE_EXCEPTIONS = True

SITE_ID = 1

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'jordanmiracle.com', 'https://www.jordanmiracle.com',
                 "https://jordanmiracle.herokuapp.com/", "*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolioapp',
    'crispy_forms',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolioproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolioproject.wsgi.application'

FIXTURES = [
    os.path.join(BASE_DIR, "fixtures")
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG:
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'USER': 'jordanmiracle',
          'NAME': 'portfoliodb',
          'HOST': 'localhost',
          'PASSWORD': 'Likeacarrot23!',
          'PORT': '5432',
      },
    }

# DATABASES = {'default': dj_database_url.config(conn_max_age=600)}


#DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.sqlite3',
#       'NAME': BASE_DIR / 'db.sqlite3',
#   }
#}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = [
#    BASE_DIR / "static"
# ]
# STATIC_ROOT = BASE_DIR / "static"
#
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES = [
#    BASE_DIR / 'static'
# ]


# MEDIA_ROOT = BASE_DIR / 'static/images'
# MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


###### AWS Settings  ######

def get_secret():
    secret_name = "jordanmiraclebucket"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])


### AWS S3 ###

# Django storages configuration

AWS_STORAGE_BUCKET_NAME = 'jordanmiraclebucket'
AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
 }
AWS_MEDIA_LOCATION = 'media'
AWS_PUBLIC_LOCATION = 'public'
PRIVATE_FILE_STORAGE = 'portfolioproject.storage_backends.MediaStorage'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'




#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
# STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
# ]

#if not DEBUG:
#    django_heroku.settings(locals(), staticfiles=False)
#    DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
# STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )

# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
# ]


### Logging ###

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'formatters': {
#        'verbose': {
#            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
#                       'pathname=%(pathname)s lineno=%(lineno)s ' +
#                       'funcname=%(funcName)s %(message)s'),
#            'datefmt': '%Y-%m-%d %H:%M:%S'
#        },
#        'simple': {
#            'format': '%(levelname)s %(message)s'
#        }
#    },
#    'handlers': {
#        'null': {
#            'level': 'DEBUG',
#            'class': 'logging.NullHandler',
#        },
#        'console': {
#            'level': 'DEBUG',
#            'class': 'logging.StreamHandler',
#            'formatter': 'verbose'
#        }
#    },
#    'loggers': {
#        'testlogger': {
#            'handlers': ['console'],
#            'level': 'INFO',
#        }
#    }
#}
