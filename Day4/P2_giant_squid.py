# Manuell die erste Reihe definieren
nums = "91,17,64,45,8,13,47,19,52,68,63,76,82,44,28,56,37,2,78,48,32,58,72,53,9,85,77,89,36,22,49,86,51,99,6,92,80,87,7,25,31,66,84,4,98,67,46,61,59,79,0,3,38,27,23,95,20,35,14,30,26,33,42,93,12,57,11,54,50,75,90,41,88,96,40,81,24,94,18,39,70,34,21,55,5,29,71,83,1,60,74,69,10,62,43,73,97,65,15,16"
nums = list(map(int, nums.split(",")))

# Boards definieren
grids = []
for board in open("./Day4/bingo_data_without_draw.txt").read().split("\n\n"):
    grid = []
    for line in board.splitlines():
        row = list(map(int, line.split()))
        grid.append(row)
    grids.append(grid)


# Zwei Arten zu gewinnen, reihen und spalten
def has_won(grid, marked):
    rows = grid
    cols = zip(*grid)

    candidates = rows
    candidates.extend(cols)

    for line in candidates:
        if all(x in marked for x in line):
            return True
    return False


def nums_not_marked(grid, marked):
    all_nums = set()
    for row in grid:
        for x in row:
            all_nums.add(x)
    return sum(all_nums - set(marked))


n = len(grids)

marked = []
for i, num in enumerate(nums):
    marked.append(num)
    for grid in grids:
        if has_won(grid, marked):
            grids.remove(grid)
            # print(num * nums_not_marked(grid, marked))
            # exit()

        if len(grids) == 0:
            print("Last Board to Win:")
            print(num * nums_not_marked(grid, marked))
            exit()
