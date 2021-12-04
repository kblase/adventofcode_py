from pathlib import Path
import sys
from collections import Counter


def read_data():
    try:
        data_file_path = sys.argv[1]
        print("-------------------------------------------------------")
        print("Using specified Movements File")
        print("-------------------------------------------------------")
    except:
        data_file_path = str(Path(__file__).parent) + "/binary_data.txt"
        print("-------------------------------------------------------")
        print("Use Script Location for Data File!")
        print("Other Filename can be passed as first CLI Argument")
        print("-------------------------------------------------------")
    read_data.data = open(data_file_path, "r").readlines()
    read_data.data = [line.rstrip() for line in read_data.data]
    return read_data.data


# def find_most_common(x):
#     return Counter(x).most_common()[0][0]

# def find_least_common(x):
#     return Counter(x).most_common()[1][0]

# def life_support_rating():
#     read_data()
#     oxygen_generator_rate = read_data.data
#     c02_scrubber_rate = ""
#     for index in range(len(read_data.data[0])):
#         s = ""
#         for line in read_data.data:
#             s += line[index]
#         print(Counter(s).most_common()[0][0])
#         list_most_common = append()
#         list_least_common =


def oxygen_generator():
    list = read_data()
    oxygen_generation = ""
    s = []
    index = 0
    while index < 12:
        print("Anzahl Durchläufe", index + 1)
        s.append([])
        for line in list:
            s[index] += line[index]
        # print(s[index])
        # print(Counter(s[index]).most_common()[0][1])
        # print(Counter(s[index]).most_common()[1][1])
        if (
            Counter(s[index]).most_common()[0][1]
            == Counter(s[index]).most_common()[1][1]
        ):
            list = [x for x in list if x[index] == "1"]
        else:
            list = [
                x
                for x in list
                if x[index] == str(Counter(s[index]).most_common()[0][0])
            ]
        if len(list) == 1:
            return list[0]
        # print(list)
        index += 1


def co2_scrubber():
    list = read_data()
    co2_scrubbing = ""
    s = []
    index = 0
    while index < 12:
        print("Anzahl Durchläufe", index + 1)
        s.append([])
        for line in list:
            s[index] += line[index]
        # print(s[index])
        # print(Counter(s[index]).most_common()[0][1])
        # print(Counter(s[index]).most_common()[1][1])
        if (
            Counter(s[index]).most_common()[0][1]
            == Counter(s[index]).most_common()[1][1]
        ):
            list = [x for x in list if x[index] == "0"]
        else:
            list = [
                x
                for x in list
                if x[index] == str(Counter(s[index]).most_common()[1][0])
            ]
        # print(list)
        if len(list) == 1:
            return list[0]
        index += 1


print("Life Support Rating is:", int(oxygen_generator(), 2) * int(co2_scrubber(), 2))
