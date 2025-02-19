from celery import Celery
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",  # Redis as the message broker
    backend="redis://localhost:6379/0"  # Storing results in Redis
)

celery = Celery("worker")
celery.conf.broker_url = "redis://localhost:6379/0"
celery.conf.result_backend = "redis://localhost:6379/0"

_P = ParamSpec("_P")
_R = TypeVar("_R")

@celery_app.task
def send_email(recipient: str, subject: str, message: str):
    print(f"Sending email to {recipient}: {subject}\n{message}")
    return f"Email sent to {recipient}"