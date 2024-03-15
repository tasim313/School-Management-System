from .auth import BASE_DIR
import os

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project101',        
        'USER': 'tasim',           
        'PASSWORD': 'tasim*#2024',    
        'HOST': 'postgres_1',           
        'PORT': '5432',               
    }
}