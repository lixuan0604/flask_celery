# 如果使用 redis 作为中间人
# broker_url = 'redis://172.16.10.7:6381/0'

# backend = 'redis://172.16.10.7:6381/1'


BROKER_URL = "redis://127.0.0.1:6379/0"

CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/1"
