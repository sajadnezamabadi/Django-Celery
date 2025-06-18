from dcelery.celery_config import app

from time import sleep 

import sys


'''
run this file :
docker exec -it django /bin/sh
python manage.py shell  
from dcelery.celery_tasks.ex7_timeout import long_running_task
long_running_task()

from dcelery.celery_tasks.ex7_timeout import excute_task_complete
excute_task_complete()
'''

@app.task(queue="tasks", time_limit=10)
def long_running_task():
    sleep(6)
    return "Task completed successfully"

@app.task(queue="tasks" , bind=True)
def proccess_task_result(self,result):
    if result is None:
        return "Task was revoked, no result to process"
    else:
        return f"Processed result: {result}"

def excute_task_complete():
    result = long_running_task.delay()
    try:
        task_result = result.get(timeout=4)
    
    except TimeoutError:
        print("Task timed out")
        sys.exit(1)

    task= long_running_task.delay()
    task.revoke(terminate=True)
    sleep(2)    
    sys.stdout.write(task.status)

    if task.status == "REVOKED":
        proccess_task_result.delay(None) #task was revoked , process accordingly
    else:
        proccess_task_result.delay(task_result)

