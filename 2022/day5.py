from pathlib import Path
import re
from argparse import ArgumentParser

current_day = "5"


def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        stacks, moves = [i.splitlines() for i in data.read().split('\n\n')]
    stacks.pop()
    stacks = [[_[i:i+4].strip(" []\n")
               for i in range(0, len(_), 4)] for _ in stacks]
    stacks_correct = []
    for i in range(len(stacks[0])):
        stacks_correct.append([])
        stacks_correct[i] = list(reversed([stacks[_][i]
                                 for _ in range(len(stacks))]))
        while "" in stacks_correct[i]:
            stacks_correct[i].remove("")
    stacks = stacks_correct
    moves = [[int(_) for _ in re.findall(r'\d+', i)] for i in moves]
    return stacks, moves


def puzzle_a(input):
    stacks = input[0]
    moves = input[1]
    for move in moves:
        s, f, t = move
        for _ in range(s):
            stacks[t-1].append(stacks[f-1].pop())
    tops = "".join([stack[-1] for stack in stacks])
    return tops


def puzzle_b(input):
    stacks = input[0]
    moves = input[1]
    for move in moves:
        s, f, t = move
        stacks[t-1].extend((stacks[f-1][-s:]))
        stacks[f-1] = stacks[f-1][:-s]
    tops = "".join([stack[-1] for stack in stacks])
    return tops


def main():
    parser = ArgumentParser(
        description="Löse Advend of Code Aufgaben")
    parser.add_argument('-e', '--example', action='store_true',
                        help="Toggles Example Dataset manually")
    args = parser.parse_args()
    print(f"Day {current_day}")
    filename = f"day{current_day}"
    if Path.is_file(Path(__file__).parent/f"data_input/{filename}.txt") and (not args.example):
        print("Using real Data!")
    else:
        filename = f"day{current_day}_ex"
        print("The Example Data looks like: \n")
        print(f"{read_input(filename)}\n")
    print("Puzzle a:", puzzle_a(read_input(filename)))
    print("Puzzle b:", puzzle_b(read_input(filename)))


if __name__ == "__main__":  # pragma: no cover
    main()
