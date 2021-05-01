"""Django settings for the flowreader project."""

from pathlib import Path

import django_cache_url
import dj_database_url
import environ

BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()

DEBUG = env("DEBUG", cast=bool, default=False)
PRIMARY_HOST = env("PRIMARY_HOST", cast=str, default="localhost")
SECRET_KEY = env(
    "SECRET_KEY",
    cast=str,
    default="django-insecure-k&((kg#c@45@(%^ras78a0t&9)*omai$6*42ee36+ae(ls8#(9",
)

CACHE_URL = env("REDIS_URL", cast=str, default="dummy://")
STATIC_ROOT = env("STATIC_ROOT", cast=str, default="static")
DATABASE_URL = env("DATABASE_URL", cast=str, default="sqlite:////tmp/sqlite.db")

CACHES = {"default": django_cache_url.parse(CACHE_URL)}
DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}


ALLOWED_HOSTS = [PRIMARY_HOST, "0.0.0.0"]

INSTALLED_APPS = [
    "flows",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
