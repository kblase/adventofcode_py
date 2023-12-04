from day3 import puzzle_a, puzzle_b, read_input

current_day = "3"


def test_puzzle_a_example():
    filename = f"day{current_day}_ex"
    assert puzzle_a(read_input(filename)) == 157


def test_puzzle_b_example():
    filename = f"day{current_day}_ex"
    assert puzzle_b(read_input(filename)) == 70


def test_puzzle_a():
    filename = f"day{current_day}"
    assert puzzle_a(read_input(filename)) == 7817


def test_puzzle_b():
    filename = f"day{current_day}"
    assert puzzle_b(read_input(filename)) == 2444
