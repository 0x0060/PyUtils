import unittest
from unittest.mock import MagicMock, patch
from typing import Any
from pyutils.logger.logger import Logger


class BaseTestUtilities:
    def setup(self) -> None:
        pass

    def teardown(self) -> None:
        pass


class TestUtilities(BaseTestUtilities):
    def setup(self) -> None:
        Logger.info("Setting up test environment...")

    def teardown(self) -> None:
        Logger.info("Tearing down test environment...")

    def create_mock(self, return_value: Any = None, side_effect: Any = None) -> MagicMock:
        mock = MagicMock(return_value=return_value, side_effect=side_effect)
        Logger.debug(f"Created mock with return_value={return_value} and side_effect={side_effect}")
        return mock

    def patch_method(self, target: str, return_value: Any = None):
        Logger.debug(f"Patching method {target} with return_value={return_value}")
        return patch(target, return_value=return_value)


class CoverageReporter:
    def __init__(self, directory: str):
        self.directory = directory

    def start(self) -> None:
        Logger.info(f"Starting coverage reporting for directory: {self.directory}")

    def stop(self) -> None:
        Logger.info("Stopping coverage reporting...")

    def report(self) -> None:
        Logger.info("Generating coverage report...")
