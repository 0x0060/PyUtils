import subprocess
import os
from pyutils.logger.logger import Logger


class EnvManager:
    def __init__(self, env_name: str):
        self.env_name = env_name

    def create_virtualenv(self) -> None:
        Logger.info(f"Creating virtual environment: {self.env_name}")
        try:
            subprocess.run(["python", "-m", "venv", self.env_name], check=True)
            Logger.info(f"Virtual environment '{self.env_name}' created successfully.")
        except subprocess.CalledProcessError as e:
            Logger.error(f"Failed to create virtual environment: {e}")

    def activate_virtualenv(self) -> str:
        if os.name == 'nt':
            activate_script = os.path.join(self.env_name, "Scripts", "activate.bat")
        else:
            activate_script = os.path.join(self.env_name, "bin", "activate")
        Logger.info(f"Activate your virtual environment using: {activate_script}")
        return activate_script

    def install_requirements(self, requirements_file: str) -> None:
        Logger.info(f"Installing requirements from {requirements_file}")
        try:
            subprocess.run(["pip", "install", "-r", requirements_file], check=True)
            Logger.info("Requirements installed successfully.")
        except subprocess.CalledProcessError as e:
            Logger.error(f"Failed to install requirements: {e}")
