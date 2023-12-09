from .auth import BASE_DIR
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Tasim',
        'USER': 'school',
        'PASSWORD': 'admin*#123',
        'HOST': 'localhost',  
        'PORT': '5432',    
    }
}