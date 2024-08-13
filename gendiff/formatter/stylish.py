import json

def format_stylish(d, depth=0):

    result = {}
    for key in d.keys():
        if d.get(key)['nested'] == True:
            if d.get(key)['type'] == 'unchanged':
                result['  ' + key] = format_stylish(d.get(key)['value'])
            elif d.get(key)['type'] == 'removed':
                result['- ' + key] = format_stylish(d.get(key)['value'])
            elif d.get(key)['type'] == 'added':
                result['+ ' + key] = format_stylish(d.get(key)['value'])
            # else:
            #     result['  ' + key] = format_stylish(d.get(key)['value'])

        else:
            if d.get(key)['type'] == 'added':
                result['+ ' + key] = d.get(key)['value']
            elif d.get(key)['type'] == 'removed':
                result['- ' + key] = d.get(key)['value']
            elif d[key]['type'] == 'unchanged':
                result[' ' + key] = d.get(key)['value']

    return json.dumps(result)
    #return json.dumps(result, separators=(('', ': ')) , indent = 2).replace('"', '')
