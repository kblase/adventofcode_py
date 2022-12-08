from pathlib import Path
from argparse import ArgumentParser

current_day = 7

def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
    # put data formatting here
    return lines

def getpaths(d):
    if not isinstance(d, dict):
        yield [d]
    else:
        yield from ([k] + w for k, v in d.items() for w in getpaths(v))
# result = list(getpaths(sample_dict))

def puzzle_a(input):
    directories = {}
    directories = {"/" : {}}
    print(directories)
    current_dir = "/"
    print(directories[current_dir])
    nested_dirs = []
    for line in input:
        if "$" in line:
            if "ls" in line:
                pass
            # elif "cd .." in line: # move up a folder
            #     nested_dirs.pop()
            #     current_dir = directories[current_dir].get()
            else: # move down a folder
                current_dir = line.split(" ")[-1]
                nested_dirs.append(line.split(" ")[-1])
        else:
            if "dir" in line:
                directories[current_dir] = {line.split(" ")[-1]}
            else:
                directories[current_dir] = {line.split(" ")[1]:line.split(" ")[0]}
    print (dir)
    print(directories)
    return


def puzzle_b(input):
    return

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