from pathlib import Path
from argparse import ArgumentParser

current_day = "3"


def read_input(filename):
    with open(Path(__file__).parent / f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    half_rucksacks = []
    for i in lines:
        half_rucksacks.append([])
        for hr in range(0, len(i), len(i) // 2):
            # print(i[hr : hr + len(i) // 2])
            half_rucksacks[lines.index(i)].append(i[hr: hr + len(i) // 2])
    return half_rucksacks


def puzzle_a(input):
    doubles = []
    sum_of_doubles = 0
    for i in input:
        doubles.append([])
        for char in set(i[0]):
            if char in i[1] and char.isupper():
                sum_of_doubles += ord(char.swapcase()) - 70
            elif char in i[1] and char.islower():
                sum_of_doubles += ord(char.swapcase()) - 64
    return sum_of_doubles


def puzzle_b(input):
    sum_of_groups = 0
    for i in range(0, len(input), 3):
        rucksacks = ["".join(input[i]), "".join(
            input[i + 1]), "".join(input[i + 2])]
        for char in set(rucksacks[0]):
            if char in rucksacks[1] and char in rucksacks[2]:
                if char.isupper():
                    sum_of_groups += ord(char.swapcase()) - 70
                elif char.islower():
                    sum_of_groups += ord(char.swapcase()) - 64
    return sum_of_groups


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
