import os
from pathlib import Path

# -----------------------
#  PATHS
# -----------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------
#  SECURITY
# -----------------------

DEBUG = os.environ.get("DEBUG", "False") == "True"

# Основной домен Render
ALLOWED_HOSTS = [
    '*'
]

# Если хочешь — можно включить wildcard (*)
# ALLOWED_HOSTS = ["*"]


# -----------------------
#  APPS
# -----------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # твои приложения
    'board',
]


# -----------------------
#  MIDDLEWARE
# -----------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -----------------------
#  URLS & WSGI
# -----------------------

ROOT_URLCONF = 'board_project.urls'

WSGI_APPLICATION = 'board_project.wsgi.application'


# -----------------------
#  DATABASE (SQLite)
# -----------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Render автоматически сохраняет эту базу в persistent disk, если нужно.


# -----------------------
#  PASSWORD VALIDATORS
# -----------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------
#  LANGUAGE & TIMEZONE
# -----------------------

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_TZ = True


# -----------------------
#  STATIC & MEDIA FILES
# -----------------------

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # для Render

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# -----------------------
#  DEFAULT PRIMARY KEY
# -----------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
