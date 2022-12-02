from pathlib import Path

current_day = ""


def read_input(input_file: Path):
    with open(input_file, "r") as data:
        lines = [line.strip() for line in data]
    return lines


def puzzle_a(input):
    return


def puzzle_b(input):
    return


if __name__ == "__main__":  # pragma: no cover
    print(f"Day {current_day}")
    input_file = Path(__file__).parent / f"data_input/day{current_day}_ex.txt"
    # input_file = Path(__file__).parent / f"data_input/day{current_day}.txt"
    # print(read_input(input_file))
    print("Puzzle a:", puzzle_a(read_input(input_file)))
    print("Puzzle b:", puzzle_b(read_input(input_file)))
