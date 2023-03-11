import logging
from logging import Logger
from typing import Optional

from dnd_utils.character import BaseCharacter, Character
from dnd_utils.consts import STAT_OUT_TPL


class BaseManager:
    def __init__(self, char: BaseCharacter, logger: Optional[Logger] = None):
        self._char = char
        self.logger = logger
        if not logger:
            self.logger = logging.getLogger(__name__)

    def get_stats(self):
        raise NotImplementedError

    def get_info(self):
        raise NotImplementedError

    def get_sub_info(self):
        raise NotImplementedError


class TextManager(BaseManager):
    def _get_one_stat(self, stat_name: str):
        stat_score = getattr(self._char.stats, stat_name)
        return STAT_OUT_TPL.format(
            stat_name=stat_name,
            score=stat_score,
            mod=self._char.get_stat_mod(stat_name),
        )

    def get_stats(self):
        arr = []
        for fieldname in self._char.stats.__fields__:
            stat_data = self._get_one_stat(fieldname)
            arr.append(stat_data)
            self.logger.debug(f"Getting stat: '{fieldname}', data: '{stat_data}'")
        return "\n".join(arr)

    def get_short_info(self):
        c = self._char
        return [c.name, c.char_class, c.level, c.alignment]


# TODO: JSONManager
