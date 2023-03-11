import json
from enum import Enum
from logging import config
from typing import Optional, Union


class AllowedJSONFormatsEnum(str, Enum):
    LONG_STORY_SHOT = "longstoryshot"


MAP_FORMAT_TO_EXTRACTOR = {AllowedJSONFormatsEnum.LONG_STORY_SHOT: lambda f: json.load(f)}


def parse_int_value(val: Optional[Union[int, str]]):
    if val is None:
        return 0
    if isinstance(val, int):
        return val
    if val.isdigit():
        return int(val)
    return val


LONG_STORY_SHOT_STAT_LABELS_TO_DATA = {
    "str": "strength",
    "dex": "dexterity",
    "con": "constitution",
    "int": "intelligence",
    "wis": "wisdom",
    "cha": "charisma",
}


log_config = {
    "version": 1,
    "root": {"handlers": ["console"], "level": "DEBUG"},
    "handlers": {
        "console": {
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG",
        }
    },
    "formatters": {
        "std_out": {
            "format": "[%(levelname)s] %(asctime)s | %(name)s:%(lineno)d | %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S",
        }
    },
}
config.dictConfig(log_config)


class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARN = "warn"
    ERROR = "error"
