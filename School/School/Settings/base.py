DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


PROJECT_APP = [
    'core',
    'common',
    'school_auth',
    'StudentApp',
    'TeacherApp',
    'SchoolAdminApp'
]


THIRD_PARTY_APP = [
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'drf_yasg',
    'versatileimagefield',
    'import_export',
    "corsheaders",
    "debug_toolbar",
    'django_seed',
]


INSTALLED_APPS = DJANGO_APPS+PROJECT_APP+THIRD_PARTY_APP


LANGUAGE_CODE = "en-us"

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True