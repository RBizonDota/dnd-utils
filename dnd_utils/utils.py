import json

from typing import Union, Optional
from enum import Enum


class AllowedJSONFormatsEnum(str, Enum):
    LONG_STORY_SHOT = "longstoryshot"

MAP_FORMAT_TO_EXTRACTOR = {
    AllowedJSONFormatsEnum.LONG_STORY_SHOT: lambda f: json.load(f)
}


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
    "cha": "charisma"
}