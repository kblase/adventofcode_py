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
    for l in input:
        numbers = re.findall('\d', l)
        line_sum = numbers[0] + numbers[-1]
        calibration_value += int(line_sum)
    return calibration_value


def puzzle_b(input):
    translation_dict = {
        "one": "o1e" ,
        "two": "t2o" ,
        "three": "t3e" ,
        "four": "f4r" ,
        "five": "f5e" ,
        "six": "s6x" ,
        "seven": "s7n" ,
        "eight": "e8t" ,
        "nine": "n9e"
    }
    translated_list = []
    for l in input:
        for word,integer in translation_dict.items():
            if word in l:
                l = l.replace(word, integer)
        translated_list.append(l)
    return puzzle_a(translated_list)

def main():
    parser = ArgumentParser(
        description="Löse Advent of Code Aufgaben")
    parser.add_argument('-e','--example', action='store_true', help="Toggles Example Dataset manually")
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