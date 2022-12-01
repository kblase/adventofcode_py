from pathlib import Path

current_day = 1


def read_input(input_file: Path):
    with open(input_file, "r") as data:
        content = [line.strip() for line in data]
    return content


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
    sorted_elfs = sorted(elf_sums, reverse=True)
    return sorted_elfs[0] + sorted_elfs[1] + sorted_elfs[2]


if __name__ == "__main__":  # pragma: no cover
    print(f"Day {current_day}")
    input_file = Path(__file__).parent / f"data_input/day{current_day}.txt"
    content = read_input(input_file)
    print("Puzzle a:", puzzle_a(content))
    print("Puzzle b:", puzzle_b(content))
