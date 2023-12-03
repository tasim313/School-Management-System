from .auth import BASE_DIR
import os

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'my_mysql_database',
    #     'USER': 'mysql_username',
    #     'PASSWORD': 'mysql_password',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'htwoyext',
#         'USER': 'htwoyext',
#         'PASSWORD': 'hba-014tW6JBqhAjjuVagqYg8kxvGnng',
#         'HOST': 'berry.db.elephantsql.com',
#         'PORT': 5432,
#     }
# }