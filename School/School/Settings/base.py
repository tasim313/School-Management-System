DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


PROJECT_APP = [
    "core",
    "common",
    "school_auth",
    "StudentApp",
    "TeacherApp",
    "SchoolAdminApp",
    "SubscriptionApp",
]


THIRD_PARTY_APP = [
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "drf_yasg",
    "versatileimagefield",
    "import_export",
    "corsheaders",
    "debug_toolbar",
    "django_seed",
    "axes",
    "django_filters",
]


INSTALLED_APPS = DJANGO_APPS + PROJECT_APP + THIRD_PARTY_APP


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_TZ = True


SITE_ID = 2


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3000",
    "http://localhost:5174",
    "http://localhost:5000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
    "http://195.35.21.202:3000",
    "http://195.35.21.202:3001",
    "http://localhost:5175",
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)


CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
    "http://195.35.21.202:3000",
    "http://195.35.21.202:3001",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
DCS_SESSION_COOKIE_SAMESITE = "None"


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_PATH = "/"
CSRF_COOKIE_HTTPONLY = True
