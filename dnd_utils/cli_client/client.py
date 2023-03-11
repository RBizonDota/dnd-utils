import cmd
import logging
import os
from typing import List, Optional

from tabulate import tabulate

from dnd_utils import Character, TextManager
from dnd_utils.cli_client.schemas import CharActionEnum
from dnd_utils.utils import LogLevel


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

    def _print_chars_table(self):
        char_attrs = [TextManager(ch).get_short_info() for ch in self._party]
        print(
            tabulate(
                char_attrs,
                headers=["Name", "Class", "Level", "Alignment"],
                tablefmt="orgtbl",
            )
        )
        print(f"\n Total: {len(self._party)} characters")

    def precmd(self, line: str):
        print()
        self.logger.debug(f"Got command: {line}")
        return line

    def postcmd(self, stop: bool, line: str):
        if not stop:
            print("=" * self._cols)
        return stop

    def _add_chars(self, *args):
        if not len(args):
            print("At least one path must be provided")
        chars = []
        try:
            for file_path in args:
                ch = Character.from_file(file_path)
                self.logger.debug(f"Got char {ch}")
                print(f"Character '{ch.name}' successfully imported")
                chars.append(ch)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        self._party.extend(chars)

    def do_char(self, line: str):
        action, *args = parse(line)
        if not action:
            print("Action must be provided")
            return
        if action == CharActionEnum.LIST:
            self._print_chars_table()
            return
        if action == CharActionEnum.ADD:
            self._add_chars(*args)
            return

        print(f"Unknown operation: '{action}'")

    def do_exit(self, line):
        return True

    def do_EOF(self, line):
        return True


def parse(arg):
    "Convert a series of zero or more numbers to an argument tuple"
    return arg.split()
