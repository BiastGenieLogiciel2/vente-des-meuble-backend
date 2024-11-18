from pathlib import Path
import os  # Ajoutez cette ligne pour importer le module os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7zpbm%byxjjmwvoq)u#8gyf(5i-%4ev@0x-4#%w2h4kd%d(oj2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Amoapp',
    'dashbordapp',
    'rest_framework',
    'produits',
    'connexion',
    'rest_framework.authtoken',  # Pour les tokens
    #'corsheaders',  # Pour gérer les CORS 
    'django.contrib.sites',  # Nécessaire pour django-allauth
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

ROOT_URLCONF = 'AMO.urls'

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

WSGI_APPLICATION = 'AMO.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Amo_bd',  # Le nom de ta base de données
        'USER': 'postgres',  # Le nom d'utilisateur PostgreSQL (généralement 'postgres')
        'PASSWORD': 'lucas2004@',  # Le mot de passe que tu as défini lors de l'installation
        'HOST': 'localhost',  # L'hôte de la base de données (généralement 'localhost')
        'PORT': '8085',  # Le port par défaut de PostgreSQL
    }
}


# configuration de l'envoie de l'email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'stivelucas037@gmail.com'
EMAIL_HOST_PASSWORD = 'stive2004@'
DEFAULT_FROM_EMAIL = 'AMO <stivelucas037@gmail.com>'

# configuration de JWT
INSTALLED_APPS += ['rest_framework_simplejwt']

#REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += [
   # 'rest_framework_simplejwt.authentication.JWTAuthentication',
#]

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),  # Durée de validité du token d'accès
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),    # Durée de validité du token de rafraîchissement
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),              # Préfixe des tokens dans les requêtes
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
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

# configuration de la section des cookies
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Utiliser la base de données pour les sessions
SESSION_COOKIE_AGE = 1209600  # Deux semaines
SESSION_COOKIE_SECURE = False  # Mettre à True en production


# redirection
LOGIN_REDIRECT_URL = '/dashboard/'  # URL après connexion
LOGOUT_REDIRECT_URL = '/connexion/'  # URL après déconnexion

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'

# Configuration des fichiers médias
MEDIA_URL = '/media/'  # URL publique pour accéder aux fichiers médias
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Chemin physique où les fichiers médias seront stockés

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuration du REST framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

AUTH_USER_MODEL = 'connexion.User'


