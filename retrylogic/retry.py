import time
import functools
from typing import Callable, Any, Optional
from pyutils.logger.logger import Logger


class Retry:
    def __init__(self, 
                 max_attempts: int = 3, 
                 delay: float = 1.0, 
                 backoff: float = 2.0, 
                 exceptions: tuple = (Exception,), 
                 final_callback: Optional[Callable] = None):
        self.max_attempts = max_attempts
        self.delay = delay
        self.backoff = backoff
        self.exceptions = exceptions
        self.final_callback = final_callback

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < self.max_attempts:
                try:
                    result = func(*args, **kwargs)
                    Logger.info(f"Function '{func.__name__}' succeeded on attempt {attempts + 1}.")
                    return result
                except self.exceptions as e:
                    attempts += 1
                    Logger.warning(f"Function '{func.__name__}' failed on attempt {attempts}. Error: {e}")
                    if attempts < self.max_attempts:
                        sleep_time = self.delay * (self.backoff ** (attempts - 1))
                        Logger.info(f"Retrying in {sleep_time:.2f} seconds...")
                        time.sleep(sleep_time)
            Logger.error(f"Function '{func.__name__}' failed after {self.max_attempts} attempts.")
            if self.final_callback:
                self.final_callback()
            raise e
        return wrapper
