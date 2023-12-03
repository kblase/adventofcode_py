from pathlib import Path
from argparse import ArgumentParser
import re
import numpy as np

current_day = 5


def puzzle_a(input):
    matrix = input[1]
    for val in input[0]:
        x0, y0, x1, y1 = map(int, val)
        xdir = 1 if x0 < x1 else -1
        ydir = 1 if y0 < y1 else -1
        if x0 == x1:  # horizontal
            for y in range(y0, y1 + ydir, ydir):
                matrix[y, x0] += 1
        elif y0 == y1:  # vertical
            for x in range(x0, x1 + xdir, xdir):
                matrix[y0, x] += 1
    return np.count_nonzero(matrix >= 2)


def puzzle_b(input):
    matrix = input[1]
    for val in input[0]:
        x0, y0, x1, y1 = map(int, val)
        xdir = 1 if x0 < x1 else -1
        ydir = 1 if y0 < y1 else -1
        if x0 == x1:  # horizontal
            for y in range(y0, y1 + ydir, ydir):
                matrix[y, x0] += 1
        elif y0 == y1:  # vertical
            for x in range(x0, x1 + xdir, xdir):
                matrix[y0, x] += 1
        elif x0 != x1 and y0 != y1:  # diagonal
            x = x0
            for y in range(y0, y1 + ydir, ydir):
                matrix[y, x] += 1
                x += xdir
    return np.count_nonzero(matrix >= 2)


def read_input(filename):
    with open(Path(__file__).parent / f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    input = list(
        [re.match("^(\d+),(\d+) -> (\d+),(\d+)$", line).groups()
         for line in lines]
    )
    matrix = np.zeros(
        (
            max(max(int(line[1]), int(line[3])) for line in input) + 1,  # y
            max(max(int(line[0]), int(line[2])) for line in input) + 1,  # x
        )
    )
    return input, matrix


def main():
    parser = ArgumentParser(description="Löse Advend of Code Aufgaben")
    parser.add_argument(
        "-e", "--example", action="store_true", help="Toggles Example Dataset manually"
    )
    args = parser.parse_args()
    print(f"Day {current_day}")
    filename = f"day{current_day}"
    if Path.is_file(Path(__file__).parent / f"data_input/{filename}.txt") and (
        not args.example
    ):
        print(f"Using real Data!")
    else:
        filename = f"day{current_day}_ex"
        print("The Example Data looks like: \n")
        print(f"{read_input(filename)}\n")
    print("Puzzle a:", puzzle_a(read_input(filename)))
    print("Puzzle b:", puzzle_b(read_input(filename)))


if __name__ == "__main__":  # pragma: no cover
    main()
