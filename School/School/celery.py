from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta
from time import sleep

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "School.settings")

app = Celery('School')

# Time zone
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Dhaka')

app.config_from_object(settings, namespace='CELERY_')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# Define your task here
# Configure the periodic task to run every 5 seconds
app.conf.beat_schedule = {
    "delete-expired-subscriptions": {
        "task": "SubscriptionApp.tasks.delete_expired_subscriptions",
        "schedule": crontab(minute=0, hour=0),  # 12:00 AM daily
    },
    "create-student-attendance-record": {
        "task": "core.tasks.create_student_attendance_record",
        "schedule": crontab(minute=0, hour=0),  # 12:00 AM daily
    },
}
