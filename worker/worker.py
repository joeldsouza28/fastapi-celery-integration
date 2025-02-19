from functools import wraps
from celery import Celery
import asyncio
from asgiref.sync import AsyncToSync
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar


celery = Celery("worker")
celery.conf.broker_url = "redis://localhost:6379/0"
celery.conf.result_backend = "redis://localhost:6379/0"

_P = ParamSpec("_P")
_R = TypeVar("_R")

def async_task(*args: Any, **kwargs: Any):
    def _decorator(func: Callable[..., Coroutine[Any, Any, Any]]):
        sync_call = AsyncToSync(func)

        @celery.task(*args, **kwargs)
        @wraps(func)
        def _decorated(*args, **kwargs):
            return sync_call(*args, **kwargs)

        return _decorated
    return _decorator

@async_task()
async def send_email(user_id: int):
    # Simulate async operation
    await asyncio.sleep(1)
    return f"Email sent to user {user_id}"