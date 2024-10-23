import time
import psutil
import functools
from typing import Callable
from pyutils.logger.logger import Logger


class PerformanceMonitor:
    def monitor_execution_time(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            Logger.info(f"Execution time of '{func.__name__}': {execution_time:.4f} seconds")
            return result
        return wrapper

    def get_memory_usage(self) -> float:
        process = psutil.Process()
        memory_info = process.memory_info()
        return memory_info.rss / (1024 ** 2)

    def log_memory_usage(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            memory_before = self.get_memory_usage()
            result = func(*args, **kwargs)
            memory_after = self.get_memory_usage()
            memory_used = memory_after - memory_before
            Logger.info(f"Memory usage of '{func.__name__}': {memory_used:.4f} MB")
            return result
        return wrapper
