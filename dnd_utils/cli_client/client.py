import cmd
import logging
import os
from typing import List, Optional

from dnd_utils import Character
from dnd_utils.utils import LogLevel
from dnd_utils.cli_client.commands import CharClientMixin


class CLIClient(cmd.Cmd, CharClientMixin):
    """Simple command processor example."""

    prompt = "> "

    def __init__(self, log_level: Optional[LogLevel], *args, **kwargs):
        super(CLIClient, self).__init__(*args, **kwargs)
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

    def precmd(self, line: str):
        print()
        self.logger.debug(f"Got command: {line}")
        return line

    def postcmd(self, stop: bool, line: str):
        if not stop:
            print("=" * self._cols)
        return stop

    def do_exit(self, line):
        return True

    def do_EOF(self, line):
        return True
