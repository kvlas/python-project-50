import gendiff.scripts.generate_diff

result = '{\n - follow: false\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: true\n}'


def test_plaindiff():
    """Check that User instance has the particular properties."""
    print(result)
    assert gendiff.scripts.generate_diff.generate_diff('file1.json', 'file2.json') == result
