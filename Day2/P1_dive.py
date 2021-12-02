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
    global movements
    global direction
    direction = []
    global distance
    distance = []
    movements = open(movements_file_path, "r").readlines()
    movements = [line.rstrip() for line in movements]
    for i in movements:
        direction.append(i.split()[0])
        distance.append(i.split()[1])
        # print("The direction is:", movements[i].split()[0])
        # print("The distance is.", movements[i].split()[1])


def move():
    global position_depth
    global position_horizontal
    position_depth = 0
    position_horizontal = 0
    for i in movements:
        if i.split()[0] == "forward":
            position_horizontal += int(i.split()[1])
        elif i.split()[0] == "up":
            position_depth -= int(i.split()[1])
        elif i.split()[0] == "down":
            position_depth += int(i.split()[1])


read_movements()
move()
print("The Answer is:")
print(position_depth * position_horizontal)
