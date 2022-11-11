


from datetime import timedelta
from flask import Flask, session,jsonify

from celery_tasks.email.tasks import sent_email
from celery_tasks.main import celery_app
from celery_tasks.message.tasks import sent_message
from celery.result import AsyncResult
app = Flask(__name__)



@app.route('/demo')
def index():
    name = 'lixuan'
    res = sent_email.delay(1)
    # 异步获取任务返回值
    print('id',res.id)
    print("res:", res.get())




    # email_level = sent_email.s(2)
    # email_level.apply_async(queue='celery')
    #
    # message_level = sent_message.s(3)
    # message_level.apply_async(queue='celery',priority=0)
    #
    # message_level = sent_message.s(4)
    # message_level.apply_async(queue='celery')

    return jsonify({'result':'success'})





if __name__ == '__main__':
    app.run(debug=True)
