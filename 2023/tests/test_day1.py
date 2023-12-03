from day1 import puzzle_a, puzzle_b, read_input

current_day = "1"


def test_puzzle_a_example():
    filename = f"day{current_day}_ex_a"
    assert puzzle_a(read_input(filename)) == 142


def test_puzzle_b_example():
    filename = f"day{current_day}_ex_b"
    assert puzzle_b(read_input(filename)) == 281


def test_puzzle_a():
    filename = f"day{current_day}"
    assert puzzle_a(read_input(filename)) == 54081


def test_puzzle_b():
    filename = f"day{current_day}"
    assert puzzle_b(read_input(filename)) == 54649
