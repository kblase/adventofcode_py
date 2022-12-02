from pathlib import Path
from argparse import ArgumentParser

current_day = 1


def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    # put data formatting here
    return lines


def puzzle_a(content):
    elf_sums = []
    sum = 0
    for elf in content:
        if elf == "":
            elf_sums.append(sum)
            sum = 0
        else:
            sum += int(elf)
    return max(elf_sums)


def puzzle_b(content):
    elf_sums = []
    sum = 0
    for elf in content:
        if elf == "":
            elf_sums.append(sum)
            sum = 0
        else:
            sum += int(elf)
    elf_sums.append(sum)
    sorted_elfs = sorted(elf_sums, reverse=True)
    return sorted_elfs[0] + sorted_elfs[1] + sorted_elfs[2]

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
