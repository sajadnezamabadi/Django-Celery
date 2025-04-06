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

base_dir = os.getcwd()
task_folder = os.path.join(base_dir , "dcelery" , "celery_tasks")

if os.path.exists(task_folder) and os.path.isdir(task_folder) :
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith("ex") and  filename.endswith(",.py"):
            module_name = f"dcelery.celery_tasks.{filename[:-3]}" 
            module = __import__(module_name , fromlist=["*"])
            
            for name in dir(module):
                obj = getattr(module , name)
                if callable(obj):
                    task_modules.append(f"{module_name}.{name}")
            
app.autodiscover_tasks(task_modules)


# app.conf.task_default_rate_limit = "1/m" #limit execute tasks
# app.conf.broker_transport_option = {
#     "priority": list(range(10)),
#     "sep": ":",
#     "queue_order_strategy":"priority",
# }
# app.conf.task_routes = {"cworker.tasks.task1": {"queue": "queue1"},"newapp.tasks.task2": {"queue": "queue2"}}
