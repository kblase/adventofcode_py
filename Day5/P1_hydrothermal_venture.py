# Lese Daten ein und fomatiere einträge als Integers

all_lines = []
for line in open("./Day5/vent_data.txt").read().split("\n"):
    coordinate_pair = []
    for start_end in line.split(" -> "):
        coordinate_pair.append(start_end)
    all_lines.append(coordinate_pair)

start = []
end = []
for coordinates in all_lines:
    for count, xy in enumerate(coordinates):
        if count == 0:
            start.append(xy.split(","))
        elif count == 1:
            end.append(xy.split(","))

print(start[0][0])
print(end[0][0])
print(start[0][1])
print(end[0][1])
# entferne diagonale Linien aus Liste und speicher diese in extra Liste
straight_lines_start = []
diagonal_lines_start = []
straight_lines_end = []
diagonal_lines_end = []
for i in range(len(start) - 1):
    if start[i][0] == end[i][0] or start[i][1] == end[i][1]:
        straight_lines_start.append(start[i])
        straight_lines_end.append(end[i])
    else:
        diagonal_lines_start.append(start[i])
        diagonal_lines_end.append(end[i])

print(straight_lines_start)
print(straight_lines_end)
