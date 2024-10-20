import json
import yaml


def import_file(path_to_file):
    format = path_to_file.split(".")[-1]
    if format == 'json':
        return json.load(open(path_to_file))
    elif format in ['yaml', 'yml']:
        return yaml.safe_load(open(path_to_file))
    else:
        raise TypeError('File extension error.')
