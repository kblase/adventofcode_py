from pathlib import Path
from argparse import ArgumentParser

current_day = 6


def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    line = [l for l in lines[0]]
    return line


def puzzle_a(input):
    for i in range(3, len(input)):
        if len(set(input[i-4:i])) == 4:
            return i


def puzzle_b(input):
    for i in range(14, len(input)):
        if len(set(input[i-14:i])) == 14:
            return i


def main():
    parser = ArgumentParser(
        description="Löse Advend of Code Aufgaben")
    parser.add_argument('-e', '--example', action='store_true',
                        help="Toggles Example Dataset manually")
    args = parser.parse_args()
    print(f"Day {current_day}")
    filename = f"day{current_day}"
    if Path.is_file(Path(__file__).parent/f"data_input/{filename}.txt") and (not args.example):
        print(f"Using real Data!")
    else:
        filename = f"day{current_day}_ex"
        print("The Example Data looks like: \n")
        print(f"{read_input(filename)}\n")
    print("Puzzle a:", puzzle_a(read_input(filename)))
    print("Puzzle b:", puzzle_b(read_input(filename)))


if __name__ == "__main__":  # pragma: no cover
    main()
