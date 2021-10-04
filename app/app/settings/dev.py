import os

from app.settings.components.dev_tools import * # noqa
from app.settings.components.base import * # noqa
# from app.settings.components.database import * # noqa
from app.settings.components.email import * # noqa
from app.settings.components.celery import * # noqa

DEBUG = True

ALLOWED_HOSTS = ['*', '127.0.0.1', 'localhost']

STATIC_ROOT = os.path.join(os.path.dirname('cdn/static'))
