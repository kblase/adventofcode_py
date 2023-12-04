from pathlib import Path
from argparse import ArgumentParser
import re

current_day = "1"


def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    # put data formatting here
    return lines


def puzzle_a(input):
    calibration_value = 0
    for _ in input:
        numbers = re.findall('\d', _)  # noqa: W605
        line_sum = numbers[0] + numbers[-1]
        calibration_value += int(line_sum)
    return calibration_value


def puzzle_b(input):
    translation_dict = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    translated_list = []
    for line in input:
        for word, integer in translation_dict.items():
            if word in line:
                line = line.replace(word, integer)
        translated_list.append(line)
    return puzzle_a(translated_list)


def main():
    parser = ArgumentParser(
        description="Löse Advent of Code Aufgaben")
    parser.add_argument('-e', '--example', action='store_true',
                        help="Toggles Example Dataset manually")
    args = parser.parse_args()
    print(f"Day {current_day}")
    filename = f"day{current_day}"
    if Path.is_file(Path(__file__).parent/f"data_input/{filename}.txt") and (not args.example):
        print("Using real Data!")
        print("Puzzle a:", puzzle_a(read_input(filename)))
        print("Puzzle b:", puzzle_b(read_input(filename)))
    else:
        for puzzle in 'a', 'b':
            filename = f"day{current_day}_ex_{puzzle}"
            print("The Example Data looks like: \n")
            print(f"{read_input(filename)}\n")
            if puzzle == 'a':
                print("Puzzle {puzzle}:", puzzle_a(read_input(filename)))
            else:
                print("Puzzle {puzzle}:", puzzle_b(read_input(filename)))


if __name__ == "__main__":  # pragma: no cover
    main()
