import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_transport_option = {
    "priority": list(range(10)),
    "sep": ":",
    "queue_order_stratgy":"priority",
}
# app.conf.task_routes = {"cworker.tasks.task1": {"queue": "queue1"},"newapp.tasks.task2": {"queue": "queue2"}}

app.autodiscover_tasks()
