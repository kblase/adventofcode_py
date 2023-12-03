from pathlib import Path
import numpy as np

current_day = 4


def puzzle_a(input_file: Path):
    bingo_draws, bingo_boards = format_input(input_file)
    marked = []
    for draw in bingo_draws:
        marked.append(draw)
        for board in bingo_boards:
            if has_won(board, marked):
                return draw * nums_not_marked(board, marked)


def puzzle_b(input_file: Path):
    bingo_draws, bingo_boards = format_input(input_file)
    marked = []
    for draw in bingo_draws:
        marked.append(draw)
        for board in bingo_boards:
            if has_won(board, marked):
                bingo_boards.remove(board)
            if len(bingo_boards) == 0:
                return draw * nums_not_marked(board, marked)
    return


def has_won(board, marked):
    candidates = board
    candidates.extend(zip(*board))
    for line in candidates:
        if all(x in marked for x in line):
            return True
    return False


def nums_not_marked(board, marked):
    all_nums = set()
    for row in board:
        for x in row:
            all_nums.add(x)
    return sum(all_nums - set(marked))


def format_input(input_file: Path):
    values = input_file.read_text().split("\n\n")
    values = (
        [int(i) for i in values[0].split(",")],
        [
            [[int(x) for x in row.split()] for row in board.split("\n")]
            for board in values[1:]
        ],
    )
    return values


if __name__ == "__main__":  # pragma: no cover
    print(f"Day {current_day}")
    input_file = Path(__file__).parent / \
        f"data_input/day{current_day}_example.txt"
    print("Puzzle a:", puzzle_a(input_file))
    print("Puzzle b:", puzzle_b(input_file))
