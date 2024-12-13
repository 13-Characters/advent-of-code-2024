import numpy as np
def part_1():
    grid = np.array([list(line.removesuffix("\n")) for line in open("input.txt").readlines()])
    result = 0
    coordinates = (grid == 'X').nonzero() # List of coordinates where the letter is X
    for i in range(coordinates[0].size):
        x_start = coordinates[0][i]
        y_start = coordinates[1][i]
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        for dir in directions:
            matches = True
            for j, char in enumerate("XMAS"):
                x = x_start + (dir[0] * j)
                y = y_start + (dir[1] * j)
                inBounds = (0 <= x < grid.shape[0]) and (0 <= y < grid.shape[1])
                if not inBounds or (grid[x][y] != char):
                    matches = False
                    break
            if matches:
                result += 1
    print(result)
def part_2():
    grid = np.array([list(line.removesuffix("\n")) for line in open("input.txt").readlines()])
    result = 0
    coordinates = (grid == 'A').nonzero()  # List of coordinates where the letter is A
    for i in range(coordinates[0].size):
        x = coordinates[0][i]
        y = coordinates[1][i]
        diagonals = [grid[x+dx][y+dy] for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)] if (0 <= x+dx < grid.shape[0]) and (0 <= y+dy < grid.shape[1])]
        if any([diagonals == list(x) for x in ["MMSS", "MSSM", "SSMM", "SMMS"]]):
            result += 1
    print(result)
part_1()
part_2()