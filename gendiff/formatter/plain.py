def format_plain(d, path=None, result=None):
    if path is None:
        path = ''
    if result is None:
        result = []
    for key in d.keys():
        current_path = path + key + '.'
        if d.get(key)['nested'] == True:
            if d.get(key)['type'] == 'added':
                result.append(('Property ' + current_path[:-1] + ' was added with value: [complex value]'))
            elif d.get(key)['type'] == 'removed':
                result.append(('Property ' + current_path[:-1] + ' was removed'))
            elif d.get(key)['type'] == 'changed':
                pass
            else:
                format_plain(d.get(key)['value'], current_path, result)
        else:
            if d.get(key)['type'] == 'added':
                result.append(('Property ' + current_path[:-1] + ' was added with value: ' + parse_value(d.get(key)['value'])))
            elif d.get(key)['type'] == 'removed':
                result.append(('Property ' + current_path[:-1] + ' was removed'))
            elif d.get(key)['type'] == 'changed':
                result.append(('Property ' + current_path[:-1] + ' was updated. From ' + parse_value(d.get(key)['value']['removed']) + ' to ' + parse_value(d.get(key)['value']['added'])))
            else:
                pass
    delim = "\n"   
    view = delim.join(map(str, result))
    return view

def parse_value(val):
    if type(val) is bool:
        new_val = str(val).lower()
    elif type(val) is str:
        new_val = "'" + val + "'"
    elif val is None:
        new_val = 'null'
    elif type(val) is dict:
        new_val = '[complex value]'
    else:
        new_val = str(val)
    return new_val