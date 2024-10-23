from functools import lru_cache
from typing import Callable, Any, Dict
from pyutils.logger.logger import Logger


class Cache:
    def __init__(self, max_size: int = 128):
        self.max_size = max_size

    def cached_function(self, func: Callable) -> Callable:
        @lru_cache(maxsize=self.max_size)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            Logger.info(f"Caching result for function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
            return result
        return wrapper


class RedisCache:
    def __init__(self, host: str = 'localhost', port: int = 6379):
        import redis
        self.client = redis.Redis(host=host, port=port)

    def set(self, key: str, value: Any, expire: int = 3600) -> None:
        self.client.set(key, value, ex=expire)
        Logger.info(f"Set cache for key: {key}")

    def get(self, key: str) -> Any:
        value = self.client.get(key)
        Logger.info(f"Retrieved cache for key: {key} with value: {value}")
        return value
