# Django settings for LemurAptana project.
import os

from .settings_secret import *

os.path.join(os.path.dirname(__file__), 'LemurApp')
FORCE_SCRIPT_NAME = ''

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['192.168.192.85']

ADMINS = (
  ('Tom Wiltzius', 'tom.wiltzius@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

base_project_directory = "/home/user/btp-lemur"
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# MEDIA_ROOT = base_project_directory + 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
# MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# ADMIN_MEDIA_PREFIX = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static/')
STATIC_URL = '/static/'

# Initial data loading directory
FIXTURE_DIRS = (
  base_project_directory + 'fixtures/',
)

# List of callables that know how to import templates from various sources.
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'OPTIONS': {
      'string_if_invalid': 'TEMPLATE ERROR',
      'loaders': [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
      ],
      'context_processors': (
        "django.template.context_processors.debug",
        "django.template.context_processors.i18n",
        "django.template.context_processors.media",
        "django.contrib.messages.context_processors.messages",
        "django.contrib.auth.context_processors.auth",
        "django.template.context_processors.request",
        "LemurAptana.LemurApp.context_processors.restricted_facilities",
        "LemurAptana.LemurApp.context_processors.banner_message"
      ),
    }
  },

]


MIDDLEWARE = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'LemurAptana.urls'

# Use the new test runner from Django 1.6
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Makes sessions expire when the browser is closed rather than persisting
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Django 5.0 removed the PickleSerializer, so we now use the JSON one
# https://docs.djangoproject.com/en/5.0/releases/5.0/
SESSION_SERIALIZER = 'django.core.signing.JSONSerializer'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = (
  # We do this so that django's collectstatic copies our bundles and other files to the STATIC_ROOT
  os.path.join(BASE_DIR, 'assets'),
)

WEBPACK_LOADER = {
  'DEFAULT': {
    'BUNDLE_DIR_NAME': 'bundles/',
    'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
  }
}

REST_FRAMEWORK = {
  'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
  'PAGE_SIZE': 10,
  'DEFAULT_AUTHENTICATION_CLASSES': [],
  'DEFAULT_PERMISSION_CLASSES': [],
  'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.staticfiles',
  'django.contrib.messages',
  'LemurAptana.LemurApp',
  # Uncomment the next line to enable the admin:
  'django.contrib.admin',
  # Uncomment the next line to enable admin documentation:
  'django.contrib.admindocs',
  'webpack_loader',
  'raven.contrib.django.raven_compat',
  'rest_framework',
  'debug_toolbar'
)
