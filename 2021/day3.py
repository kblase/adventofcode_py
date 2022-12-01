from pathlib import Path
from collections import Counter

current_day = 3


def puzzle_a(input_file: Path):
    values = [line for line in input_file.read_text().splitlines()]
    gamma_rate = ""
    epsilon_rate = ""
    for index in range(len(values[0])):
        s = ""
        for line in values:
            s += line[index]
        gamma_rate += Counter(s).most_common()[0][0]
        epsilon_rate += Counter(s).most_common()[1][0]
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return power_consumption


def puzzle_b(input_file: Path):
    def oxygen_generator():
        values = [line for line in input_file.read_text().splitlines()]
        oxygen = []
        index = 0
        while index < 12:
            oxygen.append([])
            for line in values:
                oxygen[index] += line[index]
            if (
                Counter(oxygen[index]).most_common()[0][1]
                == Counter(oxygen[index]).most_common()[1][1]
            ):
                values = [x for x in values if x[index] == "1"]
            else:
                values = [
                    x
                    for x in values
                    if x[index] == str(Counter(oxygen[index]).most_common()[0][0])
                ]
            if len(values) == 1:
                return values[0]
            index += 1

    def co2_scrubber():
        values = [line for line in input_file.read_text().splitlines()]
        co2 = []
        index = 0
        while index < 12:
            co2.append([])
            for line in values:
                co2[index] += line[index]
            if (
                Counter(co2[index]).most_common()[0][1]
                == Counter(co2[index]).most_common()[1][1]
            ):
                values = [x for x in values if x[index] == "0"]
            else:
                values = [
                    x
                    for x in values
                    if x[index] == str(Counter(co2[index]).most_common()[1][0])
                ]
            if len(values) == 1:
                return values[0]
            index += 1

    life_support_rate = int(oxygen_generator(), 2) * int(co2_scrubber(), 2)
    return life_support_rate


if __name__ == "__main__":  # pragma: no cover
    print(f"Day {current_day}")
    input_file = Path(__file__).parent / f"data_input/day{current_day}.txt"
    print("Puzzle a:", puzzle_a(input_file))
    print("Puzzle b:", puzzle_b(input_file))
