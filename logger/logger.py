from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


class BaseLogger(ABC):
    """Abstract base class for the Logger."""

    @staticmethod
    @abstractmethod
    def log(level: str, message: str) -> None:
        """Abstract method to log a message at a specific log level."""
        pass

    @staticmethod
    @abstractmethod
    def error(msg: str) -> None:
        """Abstract method to log error messages."""
        pass

    @staticmethod
    @abstractmethod
    def client(msg: str) -> None:
        """Abstract method to log client-related messages."""
        pass

    @staticmethod
    @abstractmethod
    def debug(msg: str) -> None:
        """Abstract method to log debug messages."""
        pass

    @staticmethod
    @abstractmethod
    def info(msg: str) -> None:
        """Abstract method to log informational messages."""
        pass


class Logger(BaseLogger):
    """Concrete implementation of the BaseLogger."""

    log_levels = {
        'INFO': 'INF',
        'DEBUG': 'DBG',
        'ERROR': 'ERR',
        'CLIENT': 'CLT'
    }

    @staticmethod
    def _get_current_time() -> str:
        """Returns the current time in a formatted string."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def log(level: str, message: str) -> None:
        """
        Finalizes and logs the message with the appropriate level and timestamp.

        Args:
            level (str): The log level (e.g., ERROR, INFO, DEBUG, CLIENT).
            message (str): The message to log.
        """
        prefix = Logger.log_levels.get(level, 'LOG')
        current_time = Logger._get_current_time()
        log_message = f"({prefix}): {current_time} - {message}"
        print(log_message)

    @staticmethod
    def error(msg: str) -> None:
        """Logs an error message."""
        Logger.log("ERROR", msg)

    @staticmethod
    def client(msg: str) -> None:
        """Logs a client-related message."""
        Logger.log("CLIENT", msg)

    @staticmethod
    def debug(msg: str) -> None:
        """Logs a debug message."""
        Logger.log("DEBUG", msg)

    @staticmethod
    def info(msg: str) -> None:
        """Logs an informational message."""
        Logger.log("INFO", msg)


