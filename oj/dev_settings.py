# coding=utf-8
import os
from utils.shortcuts import get_env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_env('POSTGRES_HOST', '127.0.0.1'),
        'PORT': get_env('POSTGRES_PORT', '5433'),
        'NAME': get_env('POSTGRES_DB', 'onlinejudge'),
        'USER': get_env('POSTGRES_USER', 'postgres'),
        'PASSWORD': get_env('POSTGRES_PASSWORD', '123456')
    }
}

REDIS_CONF = {
    'host': get_env('REDIS_HOST', '127.0.0.1'),
    'port': get_env('REDIS_PORT', '6379')
}


DEBUG = False

ALLOWED_HOSTS = ["*"]

DATA_DIR = f"{BASE_DIR}/data"
