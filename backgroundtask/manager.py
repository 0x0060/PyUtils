from celery import Celery
from pyutils.logger.logger import Logger

class TaskManager:
    def __init__(self, broker: str, backend: str):
        self.celery = Celery(__name__, broker=broker, backend=backend)

    def task(self, task_name: str):
        def decorator(func):
            @self.celery.task(name=task_name)
            def wrapper(*args, **kwargs):
                Logger.info(f"Starting task '{task_name}' with args: {args} and kwargs: {kwargs}")
                result = func(*args, **kwargs)
                Logger.info(f"Task '{task_name}' completed with result: {result}")
                return result
            return wrapper
        return decorator
