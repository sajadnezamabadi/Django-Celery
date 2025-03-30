from celery import shared_task
from time import sleep
@shared_task
def task1(queue="celery"):
    sleep(3)
    print("this is celery")
    return

@shared_task
def task2(queue="celery1"):
    sleep(3)
    print("this is celery1")
    return

@shared_task
def task3(queue="celery2"):
    sleep(3)
    print("this is celery2")
    return

@shared_task
def task4(queue="celery3"):
    sleep(4)
    print("this is celery3")
    return