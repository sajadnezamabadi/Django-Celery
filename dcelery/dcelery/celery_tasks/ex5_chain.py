from dcelery.celery_config import app
from celery import chain

"""
run this file :
docker exec -it django /bin/sh
python manage.py shell
from dcelery.celery_tasks.ex5_chain import run_tasks_chain
run_tasks_chain()
"""

@app.task(queue="tasks")
def add(x, y):
    return x + y

@app.task(queue="tasks")
def multiply(z):
    if z == 0:
        raise ValueError('Division by zero')
    return z

def run_tasks_chain():
    task_chain = chain(add.s(2, 3), multiply.s(0))
    
    result = task_chain.apply_async()
    
    result.get()
    