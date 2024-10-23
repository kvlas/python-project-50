import json
import yaml


def parse(string, extension):
    if extension == '.json':
        return json.loads(string)
    elif extension in ['.yaml', '.yml']:
        return yaml.safe_load(string)
    else:
        raise TypeError('File extension error.')
