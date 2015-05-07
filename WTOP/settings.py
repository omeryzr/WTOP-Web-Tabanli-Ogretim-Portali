"""
Django settings for WTOP project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import os.path
burasi=os.path.dirname(__file__)
ustDizin=os.path.split(burasi)[0]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b&!-__np)5$u8)bxcgo$5v23w_bqn8j+9u0np2x!vhpcd-+a13'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS =(
	os.path.join(ustDizin,'kullanici/sablonlar'),
)
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'kullanici',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'WTOP.urls'

WSGI_APPLICATION = 'WTOP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wtom',
        'USER': 'root',
        'PASSWORD': 'omer2413',
        'HOST': '',   # Or an IP Address that your DB is hosted on
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

MEDIA_ROOT = os.path.join(ustDizin,'static/resimler')

STATICFILES = (
	os.path.join(ustDizin,'static/'),
	      )
STATICFILES_DIRS = (
	os.path.join('static'),
)

LANGUAGE_CODE = 'tr-tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/


STATIC_URL = '/static/'

SITE_ID= '1'