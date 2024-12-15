# This was the solution I used to solve part 1 of Advent of Code.
def part_1():
    grid = [list(line.removesuffix("\n")) for line in open("example_input_2.txt").readlines()]
    # x is first component, y is second component, +x is right, +y is down
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    direction_index = 3 # directions[direction_index] represents the current direction of travel
    position = [(i, j) for j in range(len(grid)) for i in range(len(grid[0])) if grid[j][i] == "^"][0]
    grid[position[1]][position[0]] = "X"
    while True:
        direction = directions[direction_index]
        position = (position[0] + direction[0], position[1] + direction[1])
        x = position[0]
        y = position[1]
        if not ((0 <= position[0] < len(grid[0])) and (0 <= position[1] < len(grid))):
            break
        if grid[y][x] == "#": # If there is a collision
            position = (x - direction[0], y - direction[1])
            direction_index = (direction_index + 1) % 4 # Corresponds to a turn to the right
        grid[position[1]][position[0]] = "X"
    result = sum([line.count("X") for line in grid])
    print(result)
part_1()