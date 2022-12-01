from pathlib import Path

current_day =

def puzzle_a(input_file: Path):
    return

def puzzle_b(input_file: Path):
    return


if __name__ == "__main__": # pragma: no cover
    print(f"Day {current_day}")
    input_file = Path(__file__).parent / f"data_input/day{current_day}.txt"
    print("Puzzle a:", puzzle_a(input_file))
    print("Puzzle b:", puzzle_b(input_file))
