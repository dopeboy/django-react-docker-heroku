import django_heroku
import os
import environ
root = environ.Path(__file__) - 2                            # two folders back (/a/b/ - 2 = /)
DEFAULT_ENV_PATH = environ.Path(__file__) - 3                # default location of .env file
DEFAULT_ENV_FILE = DEFAULT_ENV_PATH.path('.env')()
env = environ.Env(DEBUG=(bool, False),)                      # set default values and casting
environ.Env.read_env(env.str('ENV_PATH', DEFAULT_ENV_FILE))  # reading .env file

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = root()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = []
CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)


# Application definition

INSTALLED_APPS = [
    # Standard Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'graphene_django',
    'corsheaders',

    # Our apps
    'django-react-docker-heroku',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
     'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django-react-docker-heroku.urls'

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

WSGI_APPLICATION = 'django-react-docker-heroku.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/code/server/static'

REACT_APP_DIR = os.path.join('client')
if not DEBUG:
    STATICFILES_DIRS = [
        os.path.join(REACT_APP_DIR, 'build', 'static'),
    ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

###################
# Custom settings, not standard in Django
###################
# Graphene

GRAPHENE = {
    'SCHEMA': 'django-react-docker-heroku.schema.schema',  # Where your Graphene schema lives
    'RELAY_CONNECTION_MAX_LIMIT': 50,
}

GRAPHQL_DEBUG = env('GRAPHQL_DEBUG', default=DEBUG)

if not DEBUG:
    django_heroku.settings(locals())
    # TODO - needs more investigation. For now:
    # https://github.com/kennethreitz/dj-database-url/issues/107
    del DATABASES['default']['OPTIONS']['sslmode']
