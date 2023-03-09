from enum import Enum


class CharActionEnum(str, Enum):
    LIST = "ls"
    INFO = "info"
    STATS = "stats"
    ADD = "add"
