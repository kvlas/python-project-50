#!/usr/bin/env python3

import argparse
from gendiff.find_diff import generate_diff


def main():
    # Parser init
    parser = argparse.ArgumentParser(description="Compares two configuration \
                                     files and shows a difference.")

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', required=False, default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        type=str, help='set format of output')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
