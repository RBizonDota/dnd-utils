import json
import pytest


TEST_FILE_TO_PARSE = 'examples/example.json'


@pytest.fixture
def json_data():
    with open(TEST_FILE_TO_PARSE, 'r') as f:
        d = json.load(f)
    return d