from celery_tasks.main import celery_app
import time

@celery_app.task(name='send_message')
def sent_message(x):
    y=1
    result = x + y
    time.sleep(20)
    return result