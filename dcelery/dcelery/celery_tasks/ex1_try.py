from dcelery.celery_config import app
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR ,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@  app.task(queue ="tasks")
def my_tasks():
    try:
        raise ConnectionError("Connection error occurred")
    except ConnectionError:
        logging.error("Connection error again")
