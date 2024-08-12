#!/usr/bin/env python3

import argparse
from gendiff.dict_diff import *

def main():
    # Parser init
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', required=False, default='plain', choices=['stylish', 'plain', 'json'], type=str, help='set format of output')

    args = parser.parse_args()
    diff = gen_diff(args.first_file, args.second_file, args.format)
    return diff

if __name__ == "__main__":
    main()

