import json
import yaml

def file_importer(path_to_file):
    format = path_to_file.split(".")[-1]
    if format == 'json':
        return json.load(open(path_to_file))
    elif format in ['yaml', 'yml']:
        return yaml.safe_load(open(path_to_file))
    else:
        print('NE TOT FORMAT')


def gen_diff(file1_path, file2_path):
    file1 = file_importer(file1_path)
    file2 = file_importer(file2_path)
    diff = gen_dict_diff(file1, file2)
    return format_dict(diff)


def gen_dict_diff(d1, d2):
    keys = d1.keys() | d2.keys()
    diff = {}
    for key in sorted(keys): 
        if key in (d1.keys() - d2.keys()):
            if isinstance(d1.get(key), dict):
                diff[key] = {"type": "removed", "nested": True, "value": gen_dict_diff(d1.get(key), {})} #nested
            else:
                diff[key] = {"type": "removed","nested": False, "value": d1.get(key)}
        elif key in (d2.keys() - d1.keys()):
            if isinstance(d2.get(key), dict):
                diff[key] = {"type": "added","nested": True, "value": gen_dict_diff({}, d2.get(key))} #nested
            else:         
                diff[key] = {"type": "added","nested": False, "value": d2.get(key)}
        elif key in d1.keys() & d2.keys():
            if isinstance(d1.get(key), dict) and isinstance(d2.get(key), dict):
                diff[key] = {"type": "unchanged", "nested": True, "value": gen_dict_diff(d1.get(key), d2.get(key))} #nested
            else:
                if d1.get(key) == d2.get(key):
                    diff[key] = {"type": "unchanged", "nested": False, "value": d1.get(key)}
                else:
                    diff[key] = {"type": "changed", "nested": False, "value": {"removed": d1.get(key), "added": d2.get(key)}}
    return diff

def format_dict(d, path=None, result=None):

    if path is None:
        path = ''
    if result is None:
        result = []

    for key in d.keys():
        current_path = path + key + '.'
        if d.get(key)['nested'] == True:
            if d.get(key)['type'] == 'added':
                result.append(('Property ' + current_path + ' was added with value: [complex value]'))
            elif d.get(key)['type'] == 'removed':
                result.append(('Property ' + current_path + ' was removed'))
            elif d.get(key)['type'] == 'changed':
                pass
            else:
                format_dict(d.get(key)['value'], current_path, result)
        else:
            if d.get(key)['type'] == 'added':
                result.append(('Property ' + current_path + ' was added with value: ' + parse_value(d.get(key)['value'])))
            elif d.get(key)['type'] == 'removed':
                result.append(('Property ' + current_path + ' was removed'))
            elif d.get(key)['type'] == 'changed':
                 result.append(('Property ' + current_path + ' was updated. From ' + parse_value(d.get(key)['value']['removed']) + ' to ' + parse_value(d.get(key)['value']['added'])))
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


