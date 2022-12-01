from pathlib import Path

current_day = 1


def puzzle_a(input_file: Path):
    values = [int(line) for line in input_file.read_text().splitlines()]
    prev_val = values[0]
    cnt = 0
    for val in values[1:]:
        if val > prev_val:
            cnt += 1
        prev_val = val
    return cnt


def puzzle_b(input_file: Path):
    values = [int(line) for line in input_file.read_text().splitlines()]
    triples = []
    cnt = 0
    for i in range(2, len(values)):
        triples.append(int(values[i - 2]) + int(values[i - 1]) + int(values[i]))
    prev_triple = triples[0]
    for triple in triples[1:]:
        if triple > prev_triple:
            cnt += 1
        prev_triple = triple
    return cnt


if __name__ == "__main__":  # pragma: no cover
    print(f"Day {current_day}")
    input_file = Path(__file__).parent / f"data_input/day{current_day}.txt"
    print("Puzzle a:", puzzle_a(input_file))
    print("Puzzle b:", puzzle_b(input_file))
