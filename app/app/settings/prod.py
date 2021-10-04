from app.settings.components.base import * # noqa
from app.settings.components.database import * # noqa
from app.settings.components.email import * # noqa
from app.settings.components.celery import * # noqa

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

STATIC_ROOT = '/var/www/tmp/static'

MEDIA_ROOT = '/var/www/tmp/media'
