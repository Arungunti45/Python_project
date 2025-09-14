import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-7)-gj$&hyxuyf+$$+d!b8p253!hqq&i_!1y(+#u3iaz)1o4qh&'
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'pages',

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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': [],   # or [BASE_DIR / "templates"] if you want a global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_processors.categories_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------
# 🔹 Static & Media settings
# ------------------------------
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",   # your global static folder (put images/css/js here)
]

STATIC_ROOT = BASE_DIR / "staticfiles"   # collectstatic output folder

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'home'    # After login → go to home
LOGOUT_REDIRECT_URL = 'login'  # After logout → go to login
LOGIN_URL = 'login'            # Used by `@login_required`

