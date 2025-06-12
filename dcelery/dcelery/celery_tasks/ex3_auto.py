from celery import Task
from dcelery.celery_config import app
import logging

"""
command : 
       docker exec -it django 
        python manage.py shell
from dcelery.celery_tasks.ex1_try import my_tasks 
my_tasks.delay()
"""

class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc ,ConnectionError):
            logging.error("Connection error occurred in task %s and send notify to admins", task_id)
        else : 
            print('{0!r} failed : {1!r}'.format(task_id, exc)) 
            # Log the exception with traceback
    
    def on_success(self, retval, task_id, args, kwargs):
        print('{0!r} succeeded with result: {1!r}'.format(task_id, retval))
        # Log the success with result
app.Task = CustomTask

logging.basicConfig(filename='app.log', level=logging.ERROR ,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@app.task(queue ="tasks" , autoretry_for =(ConnectionError,), default_retry_delay=5, retry_kwargs={'max_retries': 3})
def my_tasks():
    raise ConnectionError("Connection error occurred")
    return 