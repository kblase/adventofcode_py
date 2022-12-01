import pytest
from pathlib import Path
import importlib


@pytest.mark.parametrize(
    "day, puzzle, result",
    [
        (1, "a", 7),
        (1, "b", 5),
        (2, "a", 150),
        (2, "b", 900),
        (3, "a", 198),
        (3, "b", 230),
        (4, "a", 4512),
        (4, "b", 1924),
        (5, "a", 5),
        (5, "b", 0),
    ],
)
def test_example_input(day, puzzle, result):
    input_file = Path(__file__).parent / f"data_input/day{day}_example.txt"
    puzzle_solver = getattr(importlib.import_module(f"day{day}"), f"puzzle_{puzzle}")
    assert puzzle_solver(input_file) == result


@pytest.mark.parametrize(
    "day, puzzle, result",
    [
        (1, "a", 1564),
        (1, "b", 1611),
        (2, "a", 1962940),
        (2, "b", 1813664422),
        (3, "a", 3885894),
        (3, "b", 4375225),
        (4, "a", 60368),
        (4, "b", 17435),
    ],
)
def test_real_input(day, puzzle, result):
    input_file = Path(__file__).parent / f"data_input/day{day}.txt"
    puzzle_solver = getattr(importlib.import_module(f"day{day}"), f"puzzle_{puzzle}")
    assert puzzle_solver(input_file) == result
