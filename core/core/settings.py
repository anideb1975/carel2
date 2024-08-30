"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import platform
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e(9=nc9^c7z!a5_7e*do$llta1!mx_ehi3)-bps&3y7fm33zp-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
#CSRF_TRUSTED_ORIGINS = ["https://ce59-93-40-226-169.ngrok-free.app"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    "accounts",
    "aziende",
    "flotta",
    "assistenza",
    "checklist",
    'wizard',
    'extra_views',
    'formtools',
    'betterforms',
    "view_breadcrumbs",
    'import_export',
    'clean',
    'django_static_fontawesome',
    "crispy_forms",
    "crispy_bootstrap5", 
    "admin_model_list_order",
    "imagekit",
    'sweetify',
   
    
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


AUTH_USER_MODEL = "accounts.User"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'

ROOT_URLCONF = 'core.urls'

IMPORT_EXPORT_USE_TRANSACTIONS = True

CURRENT_DIR = os.path.dirname(__file__)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [CURRENT_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "checklist.custom_context_processor.fanomalie"
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        "OPTIONS": {
            "timeout": 20,  # 5 seconds is the default, but we can increase it to, e.g., 20s
        },
    }
}

"""
DATABASES = {
    ‘default’: {
    ‘ENGINE’: ‘django.db.backends.mysql’,
    ‘NAME’: ‘myproject’,
    ‘USER’:’yourusername’,
    ‘PASSWORD’:’yourpassword',
    ‘HOST’:’localhost’,
    ‘PORT’:’’,
    }
}
"""


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "it"

TIME_ZONE = "Europe/Rome"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "/static/"

if DEBUG:
  STATICFILES_DIRS = BASE_DIR, 'static'
else:
  STATIC_ROOT = BASE_DIR, 'static'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
   BASE_DIR / 'static', 
]


# Decommentare in produzione 
STATIC_ROOT = BASE_DIR / 'static_files'

### Sessione ####

SESSION_EXPIRE_SECONDS = 3600  # 1 hour

#Invalidate the session after the most recent/last activity:
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

#Re-direct users to another page:
SESSION_TIMEOUT_REDIRECT = 'index'

#Expire the session when the browser closes:
SESSION_EXPIRE_AT_BROWSER_CLOSE=True # Invalid session

SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60 # group by minute

### fine sessione ###

LOGOUT_REDIRECT_URL = 'index'
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
