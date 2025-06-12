from dcelery.celery_config import app
from celery import group


'''
run this file :
docker exec -it django /bin/sh
python manage.py shell
from dcelery.celery_tasks.ex4_groups_error import run_tasks
run_tasks()
'''

@app.task(queue="tasks")
def task(number):
    if number == 3:
        raise ValueError("Value error occurred in task {}".format(number))
    return "Task {} completed".format(number)

def handel_result(result):
    if result.successful():
        print(f"Result: {result.get()}")
    
    elif result.failed() and isinstance(result.result, ValueError):
        print(f"Task failed with ValueError: {result.result}")
    
    elif result.status == 'REVOKED':
        print(f"Task was revoked: {result.id}")

def run_tasks():
    task_group = group(task.s(i) for i in range(5))
    result_group = task_group.apply_async()
    result_group.get(disable_sync_subtasks=False , propagate=False)

    for result in result_group:
        handel_result(result)