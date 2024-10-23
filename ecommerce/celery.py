import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
app = Celery("ecommerce", broker="amqp://guest:guest@localhost:5672//")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
