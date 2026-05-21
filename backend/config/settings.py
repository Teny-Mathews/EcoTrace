import os
from pathlib import Path
from dotenv import load_dotenv

# Load environmental variables from your local .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-local-development-key-change-this-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-Party Architectural Tools
    'rest_framework',
    'corsheaders',
    
    # Internal Project Modules
    'users',       
    'logistics',   
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Processes incoming cross-origin headers first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# The Template configurations engine required to serve the Django Admin application portal
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
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database Engine Configuration mapping directly to local MariaDB / MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'ecotrace_db'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '3306'),
    }
}

# Core Model Configurations tracking user accounts and application constraints
AUTH_USER_MODEL = 'users.User'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password validation definitions
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization parameters
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Asset routing setup
STATIC_URL = 'static/'

# CORS Cross-Origin Parameters configuring incoming React connectivity bounds
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
]
CORS_ALLOW_CREDENTIALS = True

# 👈 Add this new block right here!
# Explicitly trust the Vite frontend to make credentialed requests
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


# ==============================================================================
# XAMPP MARIADB COMPATIBILITY PATCH
# ==============================================================================
# 1. Bypass Django's strict database version check
from django.db.backends.base.base import BaseDatabaseWrapper
BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# 2. Disable modern RETURNING syntax for older XAMPP MariaDB engines
from django.db.backends.mysql.features import DatabaseFeatures
DatabaseFeatures.can_return_columns_from_insert = property(lambda self: False)
# ==============================================================================

# ==============================================================================
# PYTHON 3.14 TEMPLATE CONTEXT COMPATIBILITY PATCH
# ==============================================================================
# Fixes 'super' object has no attribute 'dicts' during admin rendering
from django.template.context import RenderContext
import copy

original_copy = RenderContext.__copy__

def patched_copy(self):
    try:
        return original_copy(self)
    except AttributeError:
        # Fallback handling to explicitly extract context dicts in Python 3.14
        copied_context = RenderContext()
        # Accessing the internal dicts array across the inheritance chain manually
        copied_context.dicts = copy.copy(self.dicts)
        return copied_context

RenderContext.__copy__ = patched_copy
# ==============================================================================