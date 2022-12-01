from pathlib import Path
import re
import numpy as np

current_day = 5


class Line:
    def __init__(self, x0, y0, x1, y1) -> None:
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def print_lines(self):
        x0, y0, x1, y1 = self.x0, self.y0, self.x1, self.y1
        print("x0:", x0)
        print("x1:", x1)
        print("y0:", y0)
        print("y1:", y1)

    def insert(self, array, diagonally=False):
        x0, y0, x1, y1 = self.x0, self.y0, self.x1, self.y1
        xdir = 1 if x0 < x1 else -1
        ydir = 1 if y0 < y1 else -1

        if x0 != x1 and y0 == y1:
            for x in range(x0, x1 + xdir, xdir):
                array[y0, x] += 1
            return

        if y0 != y1 and x0 == x1:
            for y in range(y0, y1 + ydir, ydir):
                array[y, x0] += 1
            return

        if not diagonally:
            return


def setup_field(formated_data):
    return np.zeros(
        (
            max(max(line.y0, line.y1) for line in formated_data) + 1,
            max(max(line.x0, line.x1) for line in formated_data) + 1,
        )
    )


def puzzle_a(input_file: Path):
    values = format_input(input_file)
    for val in values:
        if val[0] == val[2]:
            print("horizontal")
            if val[1] < val[3]:
                print("--> y direction")
            elif val[1] > val[3]:
                print("#<-- y direction")
        elif val[1] == val[3]:
            print("vertical")
            if val[0] < val[2]:
                print("--> x direction")
            elif val[0] > val[2]:
                print("#<-- x direction")
        else:
            print("diagonal")
    return


def puzzle_b(input_file: Path):
    return


def format_input(input_file: Path):
    values = [line for line in input_file.read_text().splitlines()]
    return [
        Line(*map(int, re.match("^(\d+),(\d+) -> (\d+),(\d+)$", i).groups()))
        for i in values
    ]


def main():
    print(f"Day {current_day}")
    input_file = Path(__file__).parent / f"data_input/day{current_day}_example.txt"
    print(format_input(input_file))
    print(setup_field(format_input(input_file)))
    # print("Puzzle a:", puzzle_a(input_file))
    # print("Puzzle b:", puzzle_b(input_file))
    # print(format_input(input_file))


if __name__ == "__main__":  # pragma: no cover
    main()
