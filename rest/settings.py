"""
Django settings for rest project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
from decouple import config
import os
import cloudinary_storage


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-67()*kg*%sn(s%rk!&=$pry4bixxjg1dm8r)rcj-ikp-h$3f@h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*' , 'localhost', 'localhost:3000' , 'http://localhost:3000' , '.vercel.app' , 'aifans-django.onrender.com' , 'https://vpn-drab.vercel.app' , 'vpn-drab.vercel.app', 'https://vpn-drab.vercel.app,'    , 'murphy-backend.onrender.com']


# Application definition

SITE_ID = 2

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest',
    'rest_framework',
    'corsheaders',
    'storages',
    'drf_yasg',
    'cloudinary',
    'cloudinary_storage',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',



    'aifans.insights',
    'aifans.chats',
    'aifans.moderation',
    'aifans.notifications',
    'aifans.payments',
    'aifans.posts',
    'aifans.profile',
    'aifans.search',
    'aifans.subscriptions',
    'aifans.user',


    'manager.admin1'
    
    
]


SOCIALACCOUNT_PROVIDERS =  {
    "google": {
        "SCOPE" : [
            "profile",
            "email" 
        ],
        "AUTH_PARAMS" : {"access_type": "online"}
    }
    
    
    
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
    
    
    
]

ROOT_URLCONF = 'rest.urls'

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

WSGI_APPLICATION = 'rest.wsgi.application'





# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases




DATABASES = {}

if DEBUG:
    # Use SQLite for development
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
else:
    # Use PostgreSQL for production
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'murphy_vzj4',  # Database name
        'USER': 'murphy_vzj4_user',  # Database user
        'PASSWORD': 'YoLaaAJ15FI2x0Z9DglmYe6aBochJet5',  # Database password
        'HOST': 'dpg-cqpsg8bqf0us7394liu0-a.oregon-postgres.render.com',  # Database host
        'PORT': '5432',  # Database port
    }
    
# DATABASES['default'] = dj_database_url.parse("postgres://aifans_user:YBm8wQKH6BD2WDSy15cnRGc4M9C4bP4F@dpg-cp2eo36n7f5s73fgh5p0-a.oregon-postgres.render.com/aifans")
    
    # 'ENGINE': config('DB_ENGINE' , 'django.db.backends.postgresql' ),
    # 'NAME': config('DB_NAME'),
    # 'USER': config('DB_USER'),
    # 'PASSWORD': config('DB_PASSWORD'),
    # 'HOST': config('DB_HOST'),
    # 'PORT': config('DB_PORT'),
    
    
    
    
    

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'




CLOUDINARY_STORAGE = {
    'CLOUD_NAME' : 'dqpmntomn' ,
     'API_KEY' : '119738613296576' ,
     'API_SECRET' : 'DArcBzcj4FzSnV2vId5rCkXbRjc'
}


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


AUTHENTICATION_BACKENDS = [
    
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]
  
  
  
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True





# STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')







