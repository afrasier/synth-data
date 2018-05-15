"""
Django settings for synth_data project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_LOG_DIR = os.path.join(BASE_DIR, 'logs/')


def get_delineated_environment_variable(variable, default=None):
    '''
    Returns an environment variable, using the DJANGO_ENVIRONMENT_NAME variable
    as a prefix.
    '''
    env_name = os.environ.get('DJANGO_ENVIRONMENT_NAME', '')
    val = os.environ.get(f'{env_name}{variable}', None)
    if val is None:
        # Try with no env_name (this can be an issue when using runserver)
        val = os.environ.get(f'{variable}', None)
    if val is None:
        val = default
    return val


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG")

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'django_extensions',
    'rest_framework',

    # Application apps
    'synth_data.records',
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

ROOT_URLCONF = 'synth_data.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'synth_data.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'treaded': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'access': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(get_delineated_environment_variable('DJANGO_LOG_DIRECTORY', DEFAULT_LOG_DIR), get_delineated_environment_variable('DJANGO_LOG_ACCESS_NAME', 'access.log')),
            'maxBytes': int(get_delineated_environment_variable('DJANGO_LOG_ACCESS_MAX_SIZE', 1024 * 1024 * 5)),
            'backupCount': int(get_delineated_environment_variable('DJANGO_LOG_ACCESS_NUM_BACKUPS', 5)),
            'formatter': 'simple',
        },
        'db': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(get_delineated_environment_variable('DJANGO_LOG_DIRECTORY', DEFAULT_LOG_DIR), get_delineated_environment_variable('DJANGO_LOG_DB_NAME', 'db.log')),
            'maxBytes': int(get_delineated_environment_variable('DJANGO_LOG_DB_MAX_SIZE', 1024 * 1024 * 5)),
            'backupCount': int(get_delineated_environment_variable('DJANGO_LOG_DB_NUM_BACKUPS', 5)),
            'formatter': 'verbose',
        },
        'generic': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(get_delineated_environment_variable('DJANGO_LOG_DIRECTORY', DEFAULT_LOG_DIR), get_delineated_environment_variable('DJANGO_LOG_GENERIC_NAME', 'generic.log')),
            'maxBytes': int(get_delineated_environment_variable('DJANGO_LOG_GENERIC_MAX_SIZE', 1024 * 1024 * 5)),
            'backupCount': int(get_delineated_environment_variable('DJANGO_LOG_GENERIC_NUM_BACKUPS', 5)),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'console': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['console', 'access'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console', 'db'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'synth_data': {
            'handlers': ['console', 'generic'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

SHELL_PLUS_PRE_IMPORTS = [
    ('synth_data.records.factory.django', ('GivenNameFactory', 'LocationFactory', 'StreetNameFactory', 'StreetSuffixFactory', 'SecondaryAddressDesignatorFactory')),
    ('synth_data.records.factory.generated', ('NumberFactory',)),
]

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
