from pathlib import Path
from argparse import ArgumentParser
import re

current_day = "4"


def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    # put data formatting here
    return lines


def puzzle_a(input):
    points = 0
    for line in input:
        [_, winning, mine] = re.split(':|\|', line)  # noqa: W605
        overlap = len(list(set(winning.split()).intersection(mine.split())))
        if overlap >= 1:
            points += 2 ** (overlap - 1)
    return points


def puzzle_b(input):
    input = [(re.split(':|\|', line)) for line in input]  # noqa: W605
    for x in input:
        x.append(0)
    total_scratchcards = 0
    for index, scratch_card in enumerate(input):
        _, winning, mine, duplicates = scratch_card
        overlap = list(set(winning.split()).intersection(mine.split()))
        i = 0
        while i <= int(duplicates):
            for j in range(1, len(overlap)+1):
                input[index+j][-1] += 1
            i += 1
        total_scratchcards += 1 + int(duplicates)
    return total_scratchcards


def main():
    parser = ArgumentParser(
        description="Löse Advend of Code Aufgaben")
    parser.add_argument('-e', '--example', action='store_true',
                        help="Toggles Example Dataset manually")
    args = parser.parse_args()
    print(f"Day {current_day}")
    filename = f"day{current_day}"
    if Path.is_file(Path(__file__).parent/f"data_input/{filename}.txt") and (not args.example):
        print("Using real Data!")
    else:
        filename = f"day{current_day}_ex"
        print("The Example Data looks like: \n")
        print(f"{read_input(filename)}\n")
    print("Puzzle a:", puzzle_a(read_input(filename)))
    print("Puzzle b:", puzzle_b(read_input(filename)))


if __name__ == "__main__":  # pragma: no cover
    main()
