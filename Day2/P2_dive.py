from pathlib import Path
import sys

try:
    movements_file_path = sys.argv[1]
    print("-------------------------------------------------------")
    print("Using specified Movements File")
    print("-------------------------------------------------------")
except:
    movements_file_path = str(Path(__file__).parent) + "/movements_data.txt"
    print("-------------------------------------------------------")
    print("Use Script Location for Movement Data!")
    print("Other Filename can be passed as CLI Argument")
    print("-------------------------------------------------------")


def read_movements():
    read_movements.movements = open(movements_file_path, "r").readlines()
    read_movements.movements = [line.rstrip() for line in read_movements.movements]


def move():
    position_depth = 0
    position_horizontal = 0
    aim = 0
    for i in read_movements.movements:
        if i.split()[0] == "forward":
            position_horizontal += int(i.split()[1])
            position_depth += aim * int(i.split()[1])
        elif i.split()[0] == "up":
            aim -= int(i.split()[1])
        elif i.split()[0] == "down":
            aim += int(i.split()[1])
    move.product = position_depth * position_horizontal


read_movements()
move()
print("The Answer is:", move.product)
