from pathlib import Path
from argparse import ArgumentParser

current_day = "2"

rps={
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
    }
points ={
    "lost": 0,
    "draw": 3,
    "won": 6
}


def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    games = [game.split() for game in lines]
    return games


def puzzle_a(content):
    score = 0
    for round in content:
        if rps[round[0]] == rps[round[1]]:
            score += points["draw"]
        elif (rps[round[0]]-1 == rps[round[1]]) or (rps[round[0]]+2 == rps[round[1]]):
            score += points["lost"]
        else:
            score += points["won"]
        score += rps[round[1]]
    return score


def puzzle_b(content):
    score = 0
    for round in content:
        if rps[round[1]] == 2:
            score += rps[round[0]] + points["draw"]
        elif (rps[round[1]] == 1) and (rps[round[0]] in [2,3]) :
            score += rps[round[0]]-1
        elif (rps[round[1]] == 1) and (rps[round[0]] == 1) :
            score += rps[round[0]]+2
        elif (rps[round[1]] == 3) and (rps[round[0]] in [1,2]) :
            score += rps[round[0]]+1 + points["won"]
        elif (rps[round[1]] == 3) and (rps[round[0]] == 3) :
            score += rps[round[0]]-2 + points["won"]
    return score

def main():
    parser = ArgumentParser(
        description="Löse Advend of Code Aufgaben")
    parser.add_argument('-e','--example', action='store_true', help="Soll der Beispiel Datensatz benutzt werden?")
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