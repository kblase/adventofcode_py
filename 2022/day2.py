from pathlib import Path

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

def read_input(input_file: Path):
    with open(input_file, "r") as data:
        content = [line.strip() for line in data]
    games = [game.split() for game in content]
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


if __name__ == "__main__":  # pragma: no cover
    print(f"Day {current_day}")
    # input_file = Path(__file__).parent / f"data_input/day{current_day}_ex.txt"
    input_file = Path(__file__).parent / f"data_input/day{current_day}.txt"
    content = read_input(input_file)
    print("Puzzle a:", puzzle_a(content))
    print("Puzzle b:", puzzle_b(content))
