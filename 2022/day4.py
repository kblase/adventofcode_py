from pathlib import Path
from argparse import ArgumentParser

current_day = "4"


def read_input(filename):
    with open(Path(__file__).parent / f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    lines = [line.split(",") for line in lines]
    sections = [section.split("-") for line in lines for section in line]
    # put data formatting here
    return sections


def puzzle_a(input):
    reconsider = 0
    for i in range(0, len(input), 2):
        if (int(input[i][0]) <= int(input[i + 1][0])) and (
            int(input[i][1]) >= int(input[i + 1][1])
        ):
            reconsider += 1
        elif (int(input[i][0]) >= int(input[i + 1][0])) and (
            int(input[i][1]) <= int(input[i + 1][1])
        ):
            reconsider += 1
    return reconsider


def puzzle_b(input):
    reconsider = 0
    for i in range(0, len(input), 2):
        if (int(input[i + 1][0]) <= (int(input[i][0]) or int(input[i][1])) <= int(input[i + 1][1])):
            reconsider += 1
        elif (int(input[i][0]) <= (int(input[i+1][0]) or int(input[i+1][1])) <= int(input[i][1])):
            reconsider += 1
    return reconsider


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
