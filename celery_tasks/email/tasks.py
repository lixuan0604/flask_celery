

#=======================下面是所有celery要捕获的任务=============================

import time

from celery_tasks.main import celery_app

@celery_app.task(name="sent_email")
def sent_email(x):
    y = 1
    result = x + y
    time.sleep(5)
    return result

