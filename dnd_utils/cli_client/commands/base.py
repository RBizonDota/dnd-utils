import cmd
from typing import List
from logging import Logger

from dnd_utils.character import BaseCharacter


class BaseCommand(cmd.Cmd):
    def __init__(self, party: List[BaseCharacter], selected_char: BaseCharacter, logger: Logger):
        self._party = party
        self._selected_char = selected_char
        self.logger = logger
