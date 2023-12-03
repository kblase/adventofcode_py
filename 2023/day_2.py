from pathlib import Path
from argparse import ArgumentParser
import re

current_day = "2"

def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
        games = []
        for line in lines:
            game_dict = {
                "game": ''.join(re.findall(r"((?<=Game )\d+)" , line)),
                "blue": re.findall(r"(\d+(?= blue))", line),
                "red": re.findall(r"(\d+(?= red))", line),
                "green": re.findall(r"(\d+(?= green))", line)
            }
            games.append(game_dict)
    return games

def puzzle_a(input):
    possible_sum = 0
    for game in input:
        # red <= 12
        # green <=13
        # blue <=14
        if (max([int(x) for x in game['blue']]) <= 14) and (max([int(x) for x in game['green']]) <= 13) and (max([int(x) for x in game['red']]) <= 12):
            possible_sum += int(game['game'])
    return possible_sum


def puzzle_b(input):
    minimum_cubes_sum = 0
    for game in input:
        minimum_cubes = max([int(x) for x in game['blue']]) * max([int(x) for x in game['green']]) * max([int(x) for x in game['red']])
        minimum_cubes_sum += minimum_cubes
    return minimum_cubes_sum

def main():
    parser = ArgumentParser(
        description="Löse Advend of Code Aufgaben")
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