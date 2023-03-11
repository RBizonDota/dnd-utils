import cmd
from typing import List, Type
from logging import Logger

from dnd_utils.character import BaseCharacter


class BaseCommand(cmd.Cmd):
    def __init__(self, party: List[BaseCharacter], selected_char: BaseCharacter, logger: Logger, *args, **kwargs):
        super(BaseCommand, self).__init__(*args, **kwargs)
        self._party = party
        self._selected_char = selected_char
        self.logger = logger


class BaseClientMixin:
    def get_command(self, command: Type[BaseCommand]):
        cmnd = self._commands.get(command.__name__)
        if not cmnd:
            cmnd = command(self._party, self._selected_char, self.logger)
            self._commands[command.__name__] = cmnd
            return cmnd
        return cmnd