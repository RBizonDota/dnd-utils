import cmd
import logging
import os
from typing import List, Optional, Type

from tabulate import tabulate

from dnd_utils import Character, TextManager
from dnd_utils.cli_client.schemas import CharActionEnum
from dnd_utils.utils import LogLevel
from dnd_utils.cli_client.commands import BaseCommand, CharCommand

class CLIClient(cmd.Cmd):
    """Simple command processor example."""

    prompt = "> "

    def __init__(self, log_level: Optional[LogLevel]):
        super(CLIClient, self).__init__()
        self._selected_char: Optional[Character] = None
        self._party: List[Character] = []

        cols, lines = os.get_terminal_size()
        self._cols = cols
        self._lines = lines

        if not log_level:
            log_level = LogLevel.INFO
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level.value.upper())

        self._commands = {}

    def get_command(self, command: Type[BaseCommand]):
        cmnd = self._commands.get(command.__name__)
        if not cmnd:
            cmnd = command(self._party, self._selected_char, self.logger)
            self._commands[command.__name__] = cmnd
            return cmnd
        return cmnd

    def precmd(self, line: str):
        print()
        self.logger.debug(f"Got command: {line}")
        return line

    def postcmd(self, stop: bool, line: str):
        if not stop:
            print("=" * self._cols)
        return stop

    def do_char(self, line: str):
        self.get_command(CharCommand).onecmd(line)

    def do_exit(self, line):
        return True

    def do_EOF(self, line):
        return True
