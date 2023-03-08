from dnd_utils import Character
from dnd_utils.utils import AllowedJSONFormatsEnum


def test_parse_longstoryshot(json_data):
    ch = Character.from_json(json_data, format=AllowedJSONFormatsEnum.LONG_STORY_SHOT)
    assert isinstance(ch, Character)
    # TODO: add 