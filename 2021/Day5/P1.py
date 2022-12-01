#!/usr/bin/env python3
"""
Aufgabe P1 von Tag 5 im Advent of Code 2021
Erstellt am 02.09.2022
"""

import argparse
import numpy as np

def get_filecontent(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
        length = len(data)
    return data, length

def make_data_accessable(data_input):
    lines = [row.split(" -> ") for row in data_input]
    for coordinates in lines:
        ventline = coordinates[0].split(",")


    #value = [values.split(',') for values in line]
    # k = [",".join(koordinate) for koordinate in line]
    # value = [values.split(',') for values in k]
    return type(line[0][0])

def main(filename):
    print(make_data_accessable(get_filecontent(filename)[0]))

    np.zeros([get_filecontent(filename)[1],2])



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="edata.txt", help="Filename für Daten")
    args = parser.parse_args()
    main(args.file)