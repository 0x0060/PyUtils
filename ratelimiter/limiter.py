import time
from threading import Lock
from pyutils.logger.logger import Logger

class RateLimiter:
    def __init__(self, rate: float, per: float):
        self.rate = rate
        self.per = per
        self.tokens = rate
        self.last_check = time.monotonic()
        self.lock = Lock()

    def _add_tokens(self):
        now = time.monotonic()
        elapsed = now - self.last_check
        self.tokens += elapsed * (self.rate / self.per)
        if self.tokens > self.rate:
            self.tokens = self.rate
        self.last_check = now

    def acquire(self) -> bool:
        with self.lock:
            self._add_tokens()
            if self.tokens >= 1:
                self.tokens -= 1
                Logger.info("Token acquired, proceeding with request.")
                return True
            Logger.warning("Rate limit exceeded. Request denied.")
            return False
