import json

def format_stylish(d):
    prefixes = {
        'removed': '  - ',
        'added': '  + ',
        'unchanged': '    ',
        'changed': '    ',
        'nested': '    '
    }
    result = {}
    for key in d.keys():
        if d.get(key)['nested'] == True:
            if d.get(key)['type'] == 'unchanged':
                result['  ' + key] = format_stylish(d.get(key)['value'])
            elif d.get(key)['type'] == 'removed':
                result['- ' + key] = format_stylish(d.get(key)['value'])
            elif d.get(key)['type'] == 'added':
                result['+ ' + key] = format_stylish(d.get(key)['value'])
            else:
                result['  ' + key] = format_stylish(d.get(key)['value'])

        else:
            if d.get(key)['type'] == 'added':
                result['+ ' + key] = d.get(key)['value']
            elif d.get(key)['type'] == 'removed':
                result['- ' + key] = d.get(key)['value']

    return result
    # return json.dumps(result, separators=(('', ': ')) , indent = 2).replace('"', '')

        

    


    # if format == 'plain':
    #     view = plain(diff)
    # elif format == 'json':
    #     view = json_format(diff)
    # else:
    #     view = json.dumps(stylish(diff), separators=(('', ': ')) , indent = 4).replace('"', '')
    # return view

