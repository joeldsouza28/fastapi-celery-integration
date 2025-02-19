# fastapi-celery-integration

## summary :page_facing_up:
This is a simple project to demonstrate the integration of celery with fastapi to run asynchronous task in the background. As celery is synchronous in nature, it requires async functions to be converted to sync functions. 


## libraries :books:


```
amqp==5.3.1
annotated-types==0.7.0
anyio==4.8.0
asgiref==3.8.1
billiard==4.2.1
celery==5.4.0
channels==4.2.0
click==8.1.8
click-didyoumean==0.3.1
click-plugins==1.1.1
click-repl==0.3.0
Django==5.1.6
fastapi==0.115.8
flower==2.0.1
humanize==4.12.1
idna==3.10
kombu==5.4.2
prometheus_client==0.21.1
prompt_toolkit==3.0.50
pydantic==2.10.6
pydantic_core==2.27.2
python-dateutil==2.9.0.post0
pytz==2025.1
redis==5.2.1
six==1.17.0
sniffio==1.3.1
sqlparse==0.5.3
starlette==0.45.3
tornado==6.4.2
typing_extensions==4.12.2
tzdata==2025.1
vine==5.1.0
wcwidth==0.2.13
```

## steps to run :gear:
In first terminal
```
pip install -r requirements.txt
celery -A worker.worker worker --loglevel=info
```

In second terminal
```
uvicorn api:app --reload
```

