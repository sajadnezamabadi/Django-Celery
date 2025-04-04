import os
from time import sleep
from celery import Celery
from kombu import Queue , Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_queues = [
    Queue("tasks", Exchange("tasks"), routing_key="tasks",
          queue_arguments = {"x-max-priority": 10}),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

@app.task(queue="tasks")
def t1():
    sleep(1)
    return

@app.task(queue="tasks")
def t2():
    sleep(1)
    return

@app.task(queue="tasks")
def t3():
    sleep(1)
    return

app.autodiscover_tasks()


# app.conf.task_default_rate_limit = "1/m" #limit execute tasks
# app.conf.broker_transport_option = {
#     "priority": list(range(10)),
#     "sep": ":",
#     "queue_order_strategy":"priority",
# }
# app.conf.task_routes = {"cworker.tasks.task1": {"queue": "queue1"},"newapp.tasks.task2": {"queue": "queue2"}}
