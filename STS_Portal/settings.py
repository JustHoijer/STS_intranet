"""
Django settings for STS_Portal project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# for generating random&local secret key, temperorary
import os
from pathlib import Path

from ms_identity_web import IdentityWebPython
from ms_identity_web.configuration import AADConfig

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# TODO: create .env file to hold environmental variables (Secretkey, DB_HOST, DB_NAME, DB_USER, etc.)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
print(os.getcwd())
SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32))
if (
    os.getcwd() == "/home/vsts/work/1"
):  # todo: check once when actually running the pipeline
    DEBUG = False
    # SECURITY WARNING: keep the secret key used in production secret!
    # todo: create new secret key + add to azure keyvault
    SECRET_KEY = "django-insecure-m1j4q=5cjxirph1^ya^lzx%9(f0)r$ekt13d0yaz-9@0c_*)(x"
else:
    DEBUG = True
    SECRET_KEY = SECRET_KEY

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party
    "crispy_forms",
    "crispy_bootstrap5",
    # Local
    "pages.apps.PagesConfig",  # static pages, including landing page,
    "display_board.apps.DisplayBoardConfig",  # display board app
    "scheduler.apps.SchedulerConfig",  # ATE Schedule app
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "PAGE_SIZE": 10,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_AUTHENTICATION_CLASSES": [],
}

MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    # 'scheduler.customMiddleware.MyCustomMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "STS_Portal.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # "STS_Portal.context_processors.context",
            ],
        },
    },
]

WSGI_APPLICATION = "STS_Portal.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
## Configured PostgreSQL as default, create local STS_Portal_db
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "STS_Portal_db",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 1,
        },
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Los_Angeles"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
#### Updated here!
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media files (Images and others)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = "media/"
MEDIA_ROOT = "media/md"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "sts.webapps@gmail.com"
EMAIL_HOST_PASSWORD = "xkqjskybibrngmee"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = False
##########
# AAD_CONFIG = AADConfig.parse_json(file_path="mysite/aad.config.json")
# MS_IDENTITY_WEB = IdentityWebPython(AAD_CONFIG)
# ERROR_TEMPLATE = (
#    "auth/{}.html"  # for rendering 401 or other errors from msal_middleware
# )
# MIDDLEWARE.append("ms_identity_web.django.middleware.MsalMiddleware")
# deployment prep
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 3600  # https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
