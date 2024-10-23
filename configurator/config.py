import json
import os
import yaml
import toml
import configparser
from typing import Any, Dict


class Config:
    """A class to handle configuration management."""

    def __init__(self, config_file: str = None):
        """Initialize the Config with a config file path."""
        self.config_data: Dict[str, Any] = {}
        if config_file:
            self.load_from_file(config_file)

    def load_from_file(self, config_file: str) -> None:
        """Load configuration from a file."""
        file_extension = config_file.split('.')[-1]
        if file_extension == 'json':
            self.load_json(config_file)
        elif file_extension in ('yaml', 'yml'):
            self.load_yaml(config_file)
        elif file_extension == 'toml':
            self.load_toml(config_file)
        elif file_extension == 'ini':
            self.load_ini(config_file)
        else:
            raise ValueError("Unsupported file type. Use '.json', '.yaml', '.toml', or '.ini'.")

    def load_json(self, config_file: str) -> None:
        """Load configuration from a JSON file."""
        with open(config_file, 'r') as f:
            self.config_data = json.load(f)

    def load_yaml(self, config_file: str) -> None:
        """Load configuration from a YAML file."""
        with open(config_file, 'r') as f:
            self.config_data = yaml.safe_load(f)

    def load_toml(self, config_file: str) -> None:
        """Load configuration from a TOML file."""
        self.config_data = toml.load(config_file)

    def load_ini(self, config_file: str) -> None:
        """Load configuration from an INI file."""
        config = configparser.ConfigParser()
        config.read(config_file)
        self.config_data = {section: dict(config.items(section)) for section in config.sections()}

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value by key, with optional default."""
        return self.config_data.get(key, default)

    def load_from_env(self) -> None:
        """Load configurations from environment variables."""
        for key, value in os.environ.items():
            self.config_data[key] = value

    def __repr__(self) -> str:
        """String representation of the configuration data."""
        return f"Config({self.config_data})"
