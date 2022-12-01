from pathlib import Path

input_file = Path(__file__).parent / f"data_input/day4.txt"
values = input_file.read_text().split("\n\n")
values = (
    list(map(int, values[0].split(","))),
    [
        [[int(x) for x in row.split()] for row in board.split("\n")]
        for board in values[1:]
    ],
)

print(values[0][99])
print(values[1][2])
