from day5 import puzzle_a, puzzle_b, read_input

current_day = "5"

def test_input_return_values():
    filename = f"day{current_day}_ex"
    assert read_input(filename) == ([['Z', 'N'], ['M', 'C', 'D'], ['P']], [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]])

def test_puzzle_a_example():
    filename = f"day{current_day}_ex"
    assert puzzle_a(read_input(filename)) == 'CMZ'

def test_puzzle_b_example():
    filename = f"day{current_day}_ex"
    assert puzzle_b(read_input(filename)) == 'MCD'


def test_puzzle_a():
    filename = f"day{current_day}"
    assert puzzle_a(read_input(filename)) == 'QNHWJVJZW'

def test_puzzle_b():
    filename = f"day{current_day}"
    assert puzzle_b(read_input(filename)) == 'BPCZJLFJW'
