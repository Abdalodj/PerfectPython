#! /usr/bin/env python3
# coding: utf-8

import argparse

import analysis.csv as c_an
import analysis.xml as x_an


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension",
                        help="""Type of file to analyse.Is it a CSV or a XML?""")
    parser.add_argument("-d","--datafile",help="""CSV file containing pieces of information about the members of parliament""")
    return parser.parse_args()


def main():
    args = parse_arguments()
    datafile = args.datafile
    if args.extension == "csv":
        c_an.launch_analysis(datafile if args.datafile is not None else "current_mps.csv")
        # c_an.launch_analysis("current_mps.csv")
    elif args.extension == "xml":
        c_an.launch_analysis(datafile if args.datafile is not None else "SyceronBrut.xml")
        # x_an.launch_analysis("SyceronBrut.xml")

if __name__ == '__main__':
    main()
