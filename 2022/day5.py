from pathlib import Path
import re
from argparse import ArgumentParser

current_day = "5"

def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        lines = [line for line in data]
    stacks =[]
    stacks_correct = []
    stacklines = []
    moveset = []
    for l in lines:
        if l == "\n":
            lines.remove(l)
            break
        else:
            stacklines.append(l)
    for _ in range(0,len(stacklines)):
        lines.pop(0)
    stacklines.pop()
    for l in stacklines:
        stacks.append([l[i:i+4].strip(" []\n") for i in range(0, len(l), 4)])
    for i in range(len(stacks[0])):
        stacks_correct.append([])
        for l in range(len(stacks)):
            stacks_correct[i].append(stacks[l][i])
        stacks_correct[i] = list(reversed(stacks_correct[i]))
        while "" in stacks_correct[i]:
            stacks_correct[i].remove("")
    for i in lines:
        moveset.append(re.findall(r'\d+', i))
    return stacks_correct, moveset

def puzzle_a(input):
    tower = input[0]
    integer_moves = []
    for i in range(len(input[1])):
        integer_moves.append([])
        for l in input[1][i]:
            integer_moves[i].append(int(l))
    for move in integer_moves:
        for _ in range(move[0]):
            tower[move[2]-1].append(tower[move[1]-1][-1])
            tower[move[1]-1].pop()
    tops = [i[-1] for i in tower]
    return "".join(tops)


def puzzle_b(input):
    tower = input[0]
    integer_moves = []
    for i in range(len(input[1])):
        integer_moves.append([])
        for l in input[1][i]:
            integer_moves[i].append(int(l))
    for move in integer_moves:
        tower[move[2]-1].extend((tower[move[1]-1][-move[0]:]))
        i = 0
        while i < move[0]:
            tower[move[1]-1].pop()
            i += 1
    tops = [i[-1] for i in tower]
    return "".join(tops)

def main():
    parser = ArgumentParser(
        description="Löse Advend of Code Aufgaben")
    parser.add_argument('-e','--example', action='store_true', help="Toggles Example Dataset manually")
    args = parser.parse_args()
    print(f"Day {current_day}")
    filename = f"day{current_day}"
    if Path.is_file(Path(__file__).parent/f"data_input/{filename}.txt") and (not args.example):
        print(f"Using real Data!")
    else:
        filename = f"day{current_day}_ex"
        print("The Example Data looks like: \n")
        print(f"{read_input(filename)}\n")
    print("Puzzle a:", puzzle_a(read_input(filename)))
    print("Puzzle b:", puzzle_b(read_input(filename)))

if __name__ == "__main__":  # pragma: no cover
    main()