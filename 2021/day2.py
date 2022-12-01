from pathlib import Path

current_day = 2


def puzzle_a(input_file: Path):
    values = [line for line in input_file.read_text().splitlines()]
    position_depth = 0
    position_horizontal = 0
    for i in values:
        if i.split()[0] == "forward":
            position_horizontal += int(i.split()[1])
        elif i.split()[0] == "up":
            position_depth -= int(i.split()[1])
        elif i.split()[0] == "down":
            position_depth += int(i.split()[1])
    product = position_depth * position_horizontal
    return product


def puzzle_b(input_file: Path):
    values = [line for line in input_file.read_text().splitlines()]
    position_depth = 0
    position_horizontal = 0
    aim = 0
    for i in values:
        if i.split()[0] == "forward":
            position_horizontal += int(i.split()[1])
            position_depth += aim * int(i.split()[1])
        elif i.split()[0] == "up":
            aim -= int(i.split()[1])
        elif i.split()[0] == "down":
            aim += int(i.split()[1])
    product = position_depth * position_horizontal
    return product


if __name__ == "__main__":  # pragma: no cover
    print(f"Day {current_day}")
    input_file = Path(__file__).parent / f"data_input/day{current_day}.txt"
    print("Puzzle a:", puzzle_a(input_file))
    print("Puzzle b:", puzzle_b(input_file))
