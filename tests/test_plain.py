from gendiff.formatter.plain import parse_value


def test_decoding_value():
    assert parse_value(None) == 'null'
    assert parse_value(True) == 'true'
    assert parse_value({'a': 'b'}) == '[complex value]'
    assert parse_value(300) == 300