from .auth import BASE_DIR
import os

ROOT_PATH = os.path.dirname(__file__)

STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(ROOT_PATH, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_DIR = os.path.join(BASE_DIR, 'media')

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = 'http://195.35.21.202:8000/media/'
MEDIA_URL_2 = '/media/'

