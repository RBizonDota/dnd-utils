import json
import pytest


TEST_FILE_TO_PARSE = 'examples/example.json'

@pytest.fixture
def json_file_path():
    return TEST_FILE_TO_PARSE


@pytest.fixture
def json_data(json_file_path):
    with open(json_file_path, 'r') as f:
        d = json.load(f)
    return d