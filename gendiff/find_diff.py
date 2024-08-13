from gendiff.formatter import formatter
from gendiff.importer import import_file


def generate_diff(file1_path, file2_path, format='plain'):
    def compare_dict(d1, d2):
        keys = d1.keys() | d2.keys()
        diff = {}
        for key in sorted(keys): 
            if key in (d1.keys() - d2.keys()):
                if isinstance(d1.get(key), dict):
                    diff[key] = {"type": "removed", "nested": True, "value": compare_dict(d1.get(key), {})} #nested
                else:
                    diff[key] = {"type": "removed","nested": False, "value": d1.get(key)}
            elif key in (d2.keys() - d1.keys()):
                if isinstance(d2.get(key), dict):
                    diff[key] = {"type": "added","nested": True, "value": compare_dict({}, d2.get(key))} #nested
                else:         
                    diff[key] = {"type": "added","nested": False, "value": d2.get(key)}
            elif key in d1.keys() & d2.keys():
                if isinstance(d1.get(key), dict) and isinstance(d2.get(key), dict):
                    diff[key] = {"type": "unchanged", "nested": True, "value": compare_dict(d1.get(key), d2.get(key))} #nested
                else:
                    if d1.get(key) == d2.get(key):
                        diff[key] = {"type": "unchanged", "nested": False, "value": d1.get(key)}
                    else:
                        diff[key] = {"type": "changed", "nested": False, "value": {"removed": d1.get(key), "added": d2.get(key)}}
        return diff
    
    file1 = import_file(file1_path)
    file2 = import_file(file2_path)

    diff = compare_dict(file1, file2)
    return formatter(format)(diff)

