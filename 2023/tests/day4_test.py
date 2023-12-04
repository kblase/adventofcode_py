from day4 import puzzle_a, puzzle_b, read_input

current_day = "4"


def test_puzzle_a_example():
    filename = f"day{current_day}_ex"
    assert puzzle_a(read_input(filename)) == 13


def test_puzzle_b_example():
    filename = f"day{current_day}_ex"
    assert puzzle_b(read_input(filename)) == 467835


def test_puzzle_a():
    filename = f"day{current_day}"
    assert puzzle_a(read_input(filename)) == 521601


def test_puzzle_b():
    filename = f"day{current_day}"
    assert puzzle_b(read_input(filename)) == 80694070
