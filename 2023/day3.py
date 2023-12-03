from pathlib import Path
from argparse import ArgumentParser

current_day = "3"

# line_index, char_index, l = -1,0,1 for line numbers relative to line_index


def check_to_left(input, li, ci, l):
    ''' Function to check for adjecent digits in the left directions'''
    i = 1
    number = ""
    while ci - i >= 0 and input[li+l][ci-i].isdigit():
        number = input[li+l][ci-i] + number
        i += 1
    return int(number)


def check_to_right(input, li, ci, l):
    ''' Function to check for adjecent digits in the right directions'''
    i = 1
    number = ""
    while ci+i < len(input[0]) and input[li+l][ci+i].isdigit():
        number = number + input[li+l][ci+i]
        i += 1
    return int(number)


def check_to_both_directions(input, li, ci, l):
    ''' Function to check for adjecent digits in both directions'''
    i = 0
    number = ""
    while ci - i >= 0 and input[li+l][ci-i].isdigit():
        number = input[li+l][ci-i] + number
        i += 1
    i = 1
    while input[li+l][ci+i].isdigit() and ci <= len(input[li+l]):
        number = number + input[li+l][ci+i]
        i += 1
    return int(number)


def read_input(filename):
    with open(Path(__file__).parent/f"data_input/{filename}.txt", "r") as data:
        lines = [line.strip() for line in data]
        lines = [list(line) for line in lines]
    return lines


def puzzle_a(input):
    # find all Special Characters and save the positions
    symbol_position = []
    for line_index, line in enumerate(input):
        for char_index, char in enumerate(line):
            if char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                symbol_position.append([line_index, char_index])
    sum_numbers = 0
    for li, ci in symbol_position:
        # check for numbers in the same line as the symbol
        if input[li][ci-1].isdigit():
            sum_numbers += check_to_left(input, li, ci, 0)
        if input[li][ci+1].isdigit():
            sum_numbers += check_to_right(input, li, ci, 0)
        # check for numbers over and under the symbol
        for l in -1, 1:
            # directly above/underneath
            if input[li+l][ci].isdigit():
                sum_numbers += check_to_both_directions(input, li, ci, l)
            # NOT directly above/underneath but -1 AND +1 off in char_index
            elif input[li+l][ci-1].isdigit() and input[li+l][ci+1].isdigit():
                sum_numbers += check_to_left(input, li, ci, l)
                sum_numbers += check_to_right(input, li, ci, l)
            else:
                # just +1 off in char_index
                if input[li+l][ci+1].isdigit():
                    sum_numbers += check_to_right(input, li, ci, l)
                # just -1 off in char_index
                if input[li+l][ci-1].isdigit():
                    sum_numbers += check_to_left(input, li, ci, l)
    return sum_numbers


def puzzle_b(input):
    # find all Special Characters and save the positions
    symbol_position = []
    for line_index, line in enumerate(input):
        for char_index, char in enumerate(line):
            if char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                symbol_position.append([line_index, char_index, char])
    gear_result = 0
    for li, ci, gear in symbol_position:
        gear_numbers = []
        if gear == '*':
            # check for numbers in the same line as the symbol
            if input[li][ci-1].isdigit():
                gear_numbers.append(check_to_left(input, li, ci, 0))
            if input[li][ci+1].isdigit():
                gear_numbers.append(check_to_right(input, li, ci, 0))
            # check for numbers over and under the symbol
            for l in -1, 1:
                # directly above/underneath
                if input[li+l][ci].isdigit():
                    gear_numbers.append(
                        check_to_both_directions(input, li, ci, l))
                # NOT directly above/underneath but -1 AND +1 off in char_index
                elif input[li+l][ci-1].isdigit() and input[li+l][ci+1].isdigit():
                    gear_numbers.append(check_to_left(input, li, ci, l))
                    gear_numbers.append(check_to_right(input, li, ci, l))
                else:
                    # just +1 off in char_index
                    if input[li+l][ci+1].isdigit():
                        gear_numbers.append(check_to_right(input, li, ci, l))
                    # just -1 off in char_index
                    if input[li+l][ci-1].isdigit():
                        gear_numbers.append(check_to_left(input, li, ci, l))
            if len(gear_numbers) == 2:
                gear_faktor = gear_numbers[0] * gear_numbers[1]
                gear_result += gear_faktor
    return gear_result


def main():
    parser = ArgumentParser(
        description="Löse Advend of Code Aufgaben")
    parser.add_argument('-e', '--example', action='store_true',
                        help="Toggles Example Dataset manually")
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
