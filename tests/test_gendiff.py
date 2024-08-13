import pytest
from gendiff.find_diff import generate_diff

# result = '{\n - follow: false\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: true\n}'


# def test_plaindiff():
#     """Check that User instance has the particular properties."""
#     print(result)
#     assert gendiff.scripts.generate_diff.generate_diff('file1.json', 'file2.json') == result


TXT_SIMPLE_1 = 'tests/fixtures/file1.txt'
TXT_SIMPLE_2 = 'tests/fixtures/file2.txt'
JSON_SIMPLE_1 = 'tests/fixtures/simple_1.json'
JSON_SIMPLE_2 = 'tests/fixtures/simple_2.json'
JSON_COMPLEX_1 = 'tests/fixtures/file3.json'
JSON_COMPLEX_2 = 'tests/fixtures/file4.json'


def test_default_format():
    assert (generate_diff(JSON_COMPLEX_1,
                          JSON_COMPLEX_2) == generate_diff(
        JSON_COMPLEX_1, JSON_COMPLEX_2, 'plain'))

def test_unsupported_format():
    with pytest.raises(TypeError) as err:
        generate_diff(JSON_COMPLEX_1, JSON_COMPLEX_2, 'yaml')

    assert str(err.value) == 'Unsupported output format.'


def test_unsupported_extension():
    with pytest.raises(TypeError) as err:
        generate_diff(TXT_SIMPLE_1, TXT_SIMPLE_2, 'yaml')

    assert str(err.value) == 'File extension error.'