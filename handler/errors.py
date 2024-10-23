from abc import ABC, abstractmethod
from typing import Callable
from pyutils.logger.logger import Logger


class BaseErrorHandler(ABC):
    """Abstract base class for error handling."""

    @abstractmethod
    def handle_error(self, func: Callable) -> Callable:
        """Decorator to handle errors in the decorated function."""
        pass


class ErrorHandler(BaseErrorHandler):
    def handle_error(self, func: Callable) -> Callable:
        """Decorator to handle all errors in the decorated function."""
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except BaseException as e:  # Catch all exceptions
                self.log_error(f"An error occurred: {str(e)}")
                return None  # Return None or raise, based on your requirements
        return wrapper

    @staticmethod
    def log_error(error_message: str) -> None:
        """Logs the error message using Logger."""
        Logger.error(error_message)
