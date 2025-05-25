from dcelery.celery_config import app
import logging

"""
from dcelery.celery_tasks.ex1_try import my_tasks -> shell
my_tasks.delay()
"""


logging.basicConfig(filename='app.log', level=logging.ERROR ,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@app.task(queue ="tasks")
def my_tasks():
    try:
        raise ConnectionError("Connection error occurred")
    except ConnectionError:
        logging.error("Connection error again")
        raise ConnectionError()
    except ValueError:
        logging.error("value error")
        