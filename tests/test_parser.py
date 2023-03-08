from dnd_utils import Character
from dnd_utils.utils import AllowedJSONFormatsEnum


def test_parse_longstoryshot(json_data):
    ch = Character.from_json(json_data, format=AllowedJSONFormatsEnum.LONG_STORY_SHOT)
    assert isinstance(ch, Character)
    # TODO: add data checks

def test_parse_longstoryshot_default_format(json_data):
    ch = Character.from_json(json_data)
    assert isinstance(ch, Character)
    # TODO: add data checks


def test_file_longstoryshot(json_file_path):
    ch = Character.from_file(json_file_path, format=AllowedJSONFormatsEnum.LONG_STORY_SHOT)
    assert isinstance(ch, Character)
    # TODO: add data checks

