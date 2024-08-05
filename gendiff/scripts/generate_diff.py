#!/usr/bin/env python3

import json
import yaml

import argparse

def main():
    # Parser init
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=str, help='set format of output')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

def generate_diff(file_path1, file_path2):
    if file_path1.split(".")[-1] == json:
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))
    else:
        file1 = yaml.safe_load(open(file_path1))
        file2 = yaml.safe_load(open(file_path2))
    return dict_diff(file1, file2)


def dict_diff(d1, d2):
    diff = {}
    all_keys = set(d1.keys()).union(d2.keys())
    for key in sorted(all_keys):
        if key in d1 and key in d2:
             if d1[key] == d2[key]:
                 diff[f"  {key}"] = d1.get(key)
             else:
                 diff[f"- {key}"] = d1.get(key)
                 diff[f"+ {key}"] = d2.get(key)
        else:
             if d1.get(key) == None:
                 diff[f"+ {key}"] = d2.get(key)
             elif d2.get(key) == None:
                 diff[f"- {key}"] = d1.get(key)
             else: #d1.get(key) != d2.get(key):
                 diff[key] = (d1.get(key), d2.get(key))
    return json.dumps(diff, separators=(('', ': ')) , indent = 1).replace('"', '')

if __name__ == "__main__":
    main()
