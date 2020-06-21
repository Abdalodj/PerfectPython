#! /usr/bin/env python3
# coding: utf-8

import os
import logging as lg


lg.basicConfig(level=lg.DEBUG)

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)
    try:
        with open(path_to_file, 'r') as file:
            preview = file.readline()
        lg.debug(f"Yeah! We managed to read the file. Here is a preview \n{preview}")
    except FileNotFoundError as e:
        lg.critical(f'Ow :( The file was not found.\we catched {e}')


def main():
    launch_analysis('SyceronBrut.xml')


if __name__ == '__main__':
    main()
