from settings.conf import *
from pathlib import Path
import sys
import os


# ------------------------------------------------
# ... 

# ALLOWED_HOSTS = ["127.0.0.1", "ksa1sand.beget.tech"]

# ------------------------------------------------
# LOCAL IP HOST
ALLOWED_HOSTS = ['172.28.0.250', '127.0.0.1']

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------
# PATH

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'apps'))


# ------------------------------------------------
# APPS

DJANGO_AND_THIRD_PARTY_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'widget_tweaks',

    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
]

CORS_ALLOW_ALL_ORIGINS = True

PROJECT_APPS = [
    'auths.apps.AuthsConfig',
    'friends.apps.FriendsConfig',
    'chats.apps.ChatsConfig',
    'chat_groups.apps.ChatGroupsConfig',
    'posts.apps.PostsConfig',
    'profiles.apps.ProfilesConfig',
]

INSTALLED_APPS = DJANGO_AND_THIRD_PARTY_APPS + PROJECT_APPS


# ------------------------------------------------
# DATABASE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': NAME_DATEBASE,
        'USER': USER_DATEBASE,
        'PASSWORD': PASSWORD_DATEBASE,
        'HOST': HOST_DATEBASE,
        'PORT': PORT_DATEBASE,
    }
}


# ------------------------------------------------
# Middleware | Templates | Validators

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries' : {
                'staticfiles': 'django.templatetags.static', 
            }
        },
    },
]

WSGI_APPLICATION = 'deploy.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# ------------------------------------------------
# Rest

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ]
}



# ------------------------------------------------
# Other

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

USER_ONLINE_TIMEOUT = 300
USER_LASTSEEN_TIMEOUT = 60 * 60 * 24 * 7

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'auths.UserNet'