from gendiff.formatter.json import format_json
from gendiff.formatter.plain import format_plain
from gendiff.formatter.stylish import format_stylish

formaters = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json, }


def formatter(format):
    if format not in formaters:
        raise TypeError('Unsupported output format.')

    return formaters[format]