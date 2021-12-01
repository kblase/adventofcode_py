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


def add_triples():
    global triples
    triples = []
    for i in range(2, len(measurements)):
        if len(measurements) - i >= 2:
            triples.append(
                int(measurements[i - 2])
                + int(measurements[i - 1])
                + int(measurements[i])
            )


def find_increases_add():
    go_deeper = 0
    for i in range(1, len(triples)):
        if int(triples[i]) > int(triples[i - 1]):
            go_deeper += 1
    print("------------------------")
    print("Three Measurements sliding Window:")
    print("The Water depth increases", go_deeper, "times!")
    print("------------------------")


read_measurements()
add_triples()
find_increases_add()
