from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "http://195.35.21.202:8000/media/"
MEDIA_URL_2 = "/media/"
