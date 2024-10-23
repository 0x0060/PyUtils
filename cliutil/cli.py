import argparse
from typing import Callable, List, Optional
from pyutils.logger.logger import Logger


class CLIUtility:
    def __init__(self, description: str):
        self.parser = argparse.ArgumentParser(description=description)
        self.logger = Logger

    def add_command(self, name: str, help_text: str, func: Callable, *args: str, **kwargs: str):
        command_parser = self.parser.add_subparsers(dest='command').add_parser(name, help=help_text)
        
        for arg in args:
            command_parser.add_argument(arg, help=f'Argument for {name} command')

        for key, value in kwargs.items():
            command_parser.add_argument(f'--{key}', default=value, help=f'Optional argument for {name}')

        command_parser.set_defaults(func=func)

    def parse_arguments(self) -> Optional[Callable]:
        args = self.parser.parse_args()
        if hasattr(args, 'func'):
            return args.func
        else:
            self.logger.error("No command provided.")
            return None

    def execute(self):
        func = self.parse_arguments()
        if func:
            func()
