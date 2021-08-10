from app.settings.components.base import * # noqa
# from app.settings.components.database import *
from app.settings.components.dev_tools import *

DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
