from pathlib import Path
import sys

try:
    measurements_file_path = sys.argv[1]
    print("-------------------------------------------------------")
    print("Using specified measurements file")
    print("-------------------------------------------------------")
except:
    measurements_file_path = str(Path(__file__).parent) + "/measurements_data.txt"
    print("-------------------------------------------------------")
    print("Use script location for measurement data!")
    print("other filename can be passed as cli argument")
    print("-------------------------------------------------------")


def read_measurements():
    global measurements
    measurements = open(measurements_file_path).readlines()
    measurements = [line.rstrip() for line in measurements]


def find_increases():
    go_deeper_list = []
    for i in range(1, len(measurements)):
        if int(measurements[i]) > int(measurements[i - 1]):
            go_deeper_list.append(measurements[i])
    print("Solved by adding Elements and get length of list")
    print("The Water depth increases", len(go_deeper_list), "times!")
    print("------------------------")


def find_increases_add():
    go_deeper = 0
    for i in range(1, len(measurements)):
        if int(measurements[i]) > int(measurements[i - 1]):
            go_deeper += 1
    print("Solved by adding Numbers")
    print("The Water depth increases", go_deeper, "times!")
    print("------------------------")


read_measurements()
find_increases()
find_increases_add()
