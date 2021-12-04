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


def power_consumption_with_string():
    read_data()
    gamma_rate = ""
    epsilon_rate = ""
    for index in range(len(read_data.data[0])):
        s = ""
        for line in read_data.data:
            s += line[index]
        print(Counter(s).most_common())
        gamma_rate += Counter(s).most_common()[0][0]
        epsilon_rate += Counter(s).most_common()[1][0]
    print("The Power Consumption is:", int(gamma_rate, 2) * int(epsilon_rate, 2))


def power_consumption_with_array():
    read_data()
    gamma_rate = ""
    epsilon_rate = ""
    s = []
    for l in range(len(read_data.data[0])):
        s.append([])
        for i in read_data.data:
            s[l].append(i[l])
        gamma_rate += Counter(s[l]).most_common()[0][0]
        epsilon_rate += Counter(s[l]).most_common()[1][0]
    print("The Power Consumption is:", int(gamma_rate, 2) * int(epsilon_rate, 2))


power_consumption_with_string()
power_consumption_with_array()
