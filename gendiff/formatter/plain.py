import json


def format_plain(data):
    result = []
    build_plain_format(data, path='', result=result)
    return '\n'.join(result)


def build_plain_format(data, path, result):
    for key in data.keys():
        current_path = f"{path}{key}"
        node = data.get(key)
        process_node(node, current_path, result)


def process_node(node, current_path, result):
    if node.get('nested'):
        process_nested_node(node, current_path, result)
    else:
        process_leaf_node(node, current_path, result)


def process_nested_node(node, current_path, result):
    node_type = node.get('type')
    if node_type == 'added':
        message = format_added(current_path, node.get('value'))
        result.append(message)
    elif node_type == 'removed':
        message = format_removed(current_path)
        result.append(message)
    else:
        build_plain_format(node.get('value'), f"{current_path}.", result)


def process_leaf_node(node, current_path, result):
    node_type = node.get('type')
    if node_type == 'added':
        message = format_added(current_path, node.get('value'))
        result.append(message)
    elif node_type == 'removed':
        message = format_removed(current_path)
        result.append(message)
    elif node_type == 'changed':
        message = format_changed(current_path, node.get('value'))
        result.append(message)


def format_added(path, value):
    return f"Property '{path}' was added with value: {parse_value(value)}"


def format_removed(path):
    return f"Property '{path}' was removed"


def format_changed(path, value):
    old_value = parse_value(value.get('removed'))
    new_value = parse_value(value.get('added'))
    return f"Property '{path}' was updated. From {old_value} to {new_value}"


def parse_value(value):
    if isinstance(value, (bool, type(None))):
        return json.dumps(value)
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, int):
        return value
    else:
        return f"'{value}'"
