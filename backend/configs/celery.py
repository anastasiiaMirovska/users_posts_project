import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings') # щоб Celery знав, де брати конфігурації
app = Celery('settings') # прописуємо назву файлу, де сидять наші налаштування
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

