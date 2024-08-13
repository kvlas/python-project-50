import json

def format_plain(d, path=None, result=None):
    if path is None:
        path = ''
    if result is None:
        result = []
    for key in d.keys():
        current_path = path + key + '.'
        if d.get(key)['nested'] == True:
            if d.get(key)['type'] == 'added':
                result.append((f"Property {current_path[:-1]} was added with value: {parse_value(d.get(key)['value'])}"))
            elif d.get(key)['type'] == 'removed':
                result.append((f"Property {current_path[:-1]} was removed"))
            else:
                format_plain(d.get(key)['value'], current_path, result)
        else:
            if d.get(key)['type'] == 'added':
                result.append((f"Property {current_path[:-1]} was added with value: {parse_value(d.get(key)['value'])}"))
            elif d.get(key)['type'] == 'removed':
                result.append((f"Property {current_path[:-1]} was removed"))
            elif d.get(key)['type'] == 'changed':
                result.append((f"Property {current_path[:-1]} was updated. From {parse_value(d.get(key)['value']['removed'])} to {parse_value(d.get(key)['value']['added'])}"))
            else:
                pass
    delim = "\n"   
    view = delim.join(map(str, result))
    return view

def parse_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, int):
        return value
    else:
        return f"'{value}'"