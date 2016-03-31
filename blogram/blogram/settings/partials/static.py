import os
from .application import PROJECT_ROOT_DIR, BASE_DIR

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "media")
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")

STATIC_FILE_DIR = [
            os.path.join(BASE_DIR, "blogram", "static"),
        ]
