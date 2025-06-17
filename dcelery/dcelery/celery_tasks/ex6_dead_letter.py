from dcelery.celery_config import app

from celery import group


'''
for run this : 
docker-compose up -d
docker exec -it django /bin/sh
python manage.py shell
from dcelery.celery_tasks.ex6_dead_letter import run_tasks
run_tasks()
'''


app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True

@app.task(queue="tasks", bind=True)
def task1(self, x):
    try:
        if x == 0:
            raise ValueError("x cannot be zero")
    except Exception as e:
        handel_failed_task.apply_async(args=(x, str(e)))
        raise


@app.task(queue="dead_letter")
def handel_failed_task(x, exceptione):

    return f"Task failed with argument {x} due to {exceptione}"

def run_tasks():
    task_group = group(task1.s(2),
                       task1.s(0),
                       task1.s(3))
    task_group.apply_async()