import os
from decouple import config
import dj_database_url
import django_heroku
import yaml
import logging


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# logging django settings
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'production.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})

# read config file
with open("config.YAML", "r") as stream:
    try:
        config_file = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        logging.error(exc)

# extract keys using decouple module
SECRET_KEY = config_file['SECRET_KEY']
DEBUG = config_file['DEBUG']
ALLOWED_HOSTS = [config_file['ALLOWED_HOSTS']]

# Email Settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'edward.mike.anaryo@gmail.com'  # test
EMAIL_HOST_PASSWORD = 'yencommerce'  # test
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # INSTALLED APPS
    'crispy_forms',
    'phonenumber_field',
    'widget_tweaks',
    'rest_framework',
    'corsheaders',  # headers api

    # PROJECT APPS
    'dashboard',
    'accounts',
    'employee',
    'leave',
    'notifications',
    'api_services',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # django white noise settings
]

ROOT_URLCONF = 'hrsuit.urls'
# white noise static files settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
CORS_ALLOW_ALL_ORIGINS = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'hrsuit.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config_file['postgres_database']['database'],
        'USER': config_file['postgres_database']['username'],
        'PASSWORD': config_file['postgres_database']['password'],
        'HOST': config_file['postgres_database']['host'],
        'PORT': config_file['postgres_database']['port']
    }
}
# database connection check in seconds
db_from_env = dj_database_url.config(conn_max_age=1000)
DATABASES['default'].update(db_from_env)

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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Static and media files settings
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# static and media files root settings in production
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AWS S3 BUCKETS SETTINGS
X_FRAME_OPTIONS = 'SAMEORIGIN'

AWS_ACCESS_KEY_ID = config_file['AWS']['AWS_S3_BUCKET_ACCESS_ID']
AWS_SECRET_ACCESS_KEY = config_file['AWS']['AWS_S3_BUCKET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config_file['AWS']['AWS_STORAGE_BUCKET_NAME']

AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True


django_heroku.settings(locals())
