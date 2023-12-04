from pathlib import Path
from argparse import ArgumentParser
import collections

current_day = 6


def read_input(filename):
    with open(Path(__file__).parent / f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    line = list(map(int, lines[0].split(",")))
    return line


def puzzle_a(input):
    for i in range(80):
        new_fish = 0
        for _ in range(len(input)):
            input[_] -= 1
            if input[_] < 0:
                new_fish += 1
                input[_] = 6
        for new in range(new_fish):
            input.append(8)
    return len(input)


def puzzle_b(input):
    fish_totals = collections.deque(input.count(i) for i in range(9))
    for _ in range(256):
        fish_totals.rotate(-1)
        fish_totals[6] += fish_totals[8]
    return sum(fish_totals)


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
        print("Using real Data!")
    else:
        filename = f"day{current_day}_ex"
        print("The Example Data looks like: \n")
        print(f"{read_input(filename)}\n")
    print("Puzzle a:", puzzle_a(read_input(filename)))
    print("Puzzle b:", puzzle_b(read_input(filename)))


if __name__ == "__main__":  # pragma: no cover
    main()
