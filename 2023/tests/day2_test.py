from day2 import puzzle_a, puzzle_b, read_input

current_day = "2"


def test_puzzle_a_example():
    filename = f"day{current_day}_ex"
    assert puzzle_a(read_input(filename)) == 8


def test_puzzle_b_example():
    filename = f"day{current_day}_ex"
    assert puzzle_b(read_input(filename)) == 2286


def test_puzzle_a():
    filename = f"day{current_day}"
    assert puzzle_a(read_input(filename)) == 2268


def test_puzzle_b():
    filename = f"day{current_day}"
    assert puzzle_b(read_input(filename)) == 63542
