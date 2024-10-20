from gendiff.formatter import formatter
from gendiff.importer import import_file


def generate_diff(file1_path, file2_path, format='stylish'):
    file1 = import_file(file1_path)
    file2 = import_file(file2_path)
    diff = build_diff(file1, file2)
    return formatter(format)(diff)


def build_diff(d1, d2):
    diff = {}
    all_keys = get_all_keys(d1, d2)
    for key in sorted(all_keys):
        diff[key] = get_diff_node(key, d1, d2)
    return diff


def get_all_keys(d1, d2):
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise TypeError("Expected dictionaries in get_all_keys.")
    return d1.keys() | d2.keys()


def get_diff_node(key, d1, d2):
    val1 = d1.get(key)
    val2 = d2.get(key)

    if key not in d1:
        return create_added_node(val2)
    elif key not in d2:
        return create_removed_node(val1)
    else:
        if is_both_dict(val1, val2):
            return create_nested_node(build_diff(val1, val2))
        elif val1 == val2:
            return create_unchanged_node(val1)
        else:
            return create_changed_node(val1, val2)


def is_both_dict(val1, val2):
    return isinstance(val1, dict) and isinstance(val2, dict)


def create_added_node(value):
    if isinstance(value, dict):
        return {
            "type": "added",
            "nested": True,
            "value": build_diff({}, value)
        }
    else:
        return {
            "type": "added",
            "nested": False,
            "value": value
        }


def create_removed_node(value):
    if isinstance(value, dict):
        return {
            "type": "removed",
            "nested": True,
            "value": build_diff(value, {})
        }
    else:
        return {
            "type": "removed",
            "nested": False,
            "value": value
        }


def create_unchanged_node(value):
    if not isinstance(value, dict):
        return {
            "type": "unchanged",
            "nested": isinstance(value, dict),
            "value": value
        }
    else:
        return {
            "type": "unchanged",
            "nested": isinstance(value, dict),
            "value": build_diff(value, value)
        }


def create_changed_node(val1, val2):
    return {
        "type": "changed",
        "nested": False,
        "value": {
            "removed": val1,
            "added": val2
        }
    }


def create_nested_node(value):
    return {
        "type": "unchanged",
        "nested": True,
        "value": value
    }
