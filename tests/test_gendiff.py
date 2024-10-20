import pytest
from gendiff.find_diff import generate_diff


TXT_SIMPLE_1 = 'tests/fixtures/file1.txt'
TXT_SIMPLE_2 = 'tests/fixtures/file2.txt'
JSON_SIMPLE_1 = 'tests/fixtures/file1.json'
JSON_SIMPLE_2 = 'tests/fixtures/file2.json'
JSON_COMPLEX_1 = 'tests/fixtures/file3.json'
JSON_COMPLEX_2 = 'tests/fixtures/file4.json'
YAML_SIMPLE_1 = 'tests/fixtures/file1.yaml'
YAML_SIMPLE_2 = 'tests/fixtures/file2.yaml'
SIMPLE_STYLISH = 'tests/fixtures/stylish1.txt'
COMPLEX_STYLISH = 'tests/fixtures/stylish2.txt'
SIMPLE_PLAIN = 'tests/fixtures/plain1.txt'
COMPLEX_PLAIN = 'tests/fixtures/plain2.txt'
SIMPLE_JSON = 'tests/fixtures/json1.txt'
COMPLEX_JSON = 'tests/fixtures/json2.txt'


def test_default_format():
    assert (generate_diff(JSON_COMPLEX_1,
                          JSON_COMPLEX_2) == generate_diff(
        JSON_COMPLEX_1, JSON_COMPLEX_2, 'stylish'))


def test_unsupported_format():
    with pytest.raises(TypeError) as err:
        generate_diff(JSON_COMPLEX_1, JSON_COMPLEX_2, 'yaml')

    assert str(err.value) == 'Unsupported output format.'


def test_unsupported_extension():
    with pytest.raises(TypeError) as err:
        generate_diff(TXT_SIMPLE_1, TXT_SIMPLE_2, 'yaml')

    assert str(err.value) == 'File extension error.'


def read_file(format):
    return open(format, 'r').read()


@pytest.mark.parametrize('first_file, second_file, format, expected', [
    (JSON_SIMPLE_1, JSON_SIMPLE_2,
     'json', read_file(SIMPLE_JSON),),
    (JSON_COMPLEX_1, JSON_COMPLEX_2,
     'json', read_file(COMPLEX_JSON),),
    (YAML_SIMPLE_1, YAML_SIMPLE_2,
     'json', read_file(SIMPLE_JSON),),
    (JSON_SIMPLE_1, JSON_SIMPLE_2,
     'plain', read_file(SIMPLE_PLAIN),),
    (JSON_COMPLEX_1, JSON_COMPLEX_2,
     'plain', read_file(COMPLEX_PLAIN),),
    (JSON_SIMPLE_1, JSON_SIMPLE_2,
     'stylish', read_file(SIMPLE_STYLISH),),
    (JSON_COMPLEX_1, JSON_COMPLEX_2,
     'stylish', read_file(COMPLEX_STYLISH),),
    (YAML_SIMPLE_1, YAML_SIMPLE_2,
     'stylish', read_file(SIMPLE_STYLISH),),])
def test_generate_diff(first_file, second_file, format, expected):
    """Check that generate_diff output is correct."""
    assert generate_diff(first_file, second_file, format) == expected
