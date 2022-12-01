from pathlib import Path

current_day = ""


def read_input(input_file: Path):
    with open(input_file, "r") as data:
        content = [line.strip() for line in data]
    return content


def puzzle_a(content):
    return


def puzzle_b(content):
    return


if __name__ == "__main__":  # pragma: no cover
    print(f"Day {current_day}")
    input_file = Path(__file__).parent / f"data_input/day{current_day}.txt"
    content = read_input(input_file)
    print("Puzzle a:", puzzle_a(content))
    print("Puzzle b:", puzzle_b(content))
