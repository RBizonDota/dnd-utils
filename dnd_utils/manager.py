from .character import BaseCharacter, Character
from .consts import STAT_OUT_TPL


class CharacterManager:
    def __init__(self, char: BaseCharacter):
        self._char = char

    def _get_one_stat(self, stat_name: str):
        stat_score = getattr(self._char.stats, stat_name)
        mod = (stat_score-10)//2
        return STAT_OUT_TPL.format(stat_name=stat_name, score=stat_score, mod=mod)


    def get_stats(self):
        arr = []
        for fieldname in self._char.stats.__fields__:
            arr.append(self._get_one_stat(fieldname))
        return "\n".join(arr)