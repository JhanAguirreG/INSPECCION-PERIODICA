from pathlib import Path
import os

# --------------------------------------------------
# BASE
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-cambia-esto-en-produccion'

DEBUG = True

ALLOWED_HOSTS = ['*']


# --------------------------------------------------
# APLICACIONES
# --------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tu app
    'inspecciones',
]


# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --------------------------------------------------
# URLS
# --------------------------------------------------

ROOT_URLCONF = 'sighi.urls'


# --------------------------------------------------
# TEMPLATES (IMPORTANTE)
# --------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Puedes dejarlo vacío porque usaremos templates dentro de la app
        'DIRS': [],

        'APP_DIRS': True,  # 🔥 ESTO DEBE ESTAR EN TRUE

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


# --------------------------------------------------
# WSGI
# --------------------------------------------------

WSGI_APPLICATION = 'sighi.wsgi.application'


# --------------------------------------------------
# BASE DE DATOS
# --------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --------------------------------------------------
# VALIDACIÓN DE PASSWORD
# --------------------------------------------------

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


# --------------------------------------------------
# INTERNACIONALIZACIÓN
# --------------------------------------------------

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True
USE_TZ = True


# --------------------------------------------------
# ARCHIVOS ESTÁTICOS
# --------------------------------------------------

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# --------------------------------------------------
# ARCHIVOS MEDIA (PDFS Y FIRMAS)
# --------------------------------------------------

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# --------------------------------------------------
# LOGIN
# --------------------------------------------------
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/inspecciones/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'
#LOGIN_REDIRECT_URL = '/inspecciones/'


# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
