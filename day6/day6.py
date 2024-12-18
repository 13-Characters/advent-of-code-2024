grid = [list(line.removesuffix("\n")) for line in open("input.txt").readlines()]

def inBounds(x, y):
    return (0 <= x < len(grid[0])) and (0 <= y < len(grid))
def part_1(grid, output_result=False):
    grid_temp = [line.copy() for line in grid]
    # x is first component, y is second component, +x is right, +y is down
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_index = 3  # directions[direction_index] represents the current direction of travel
    position = [(i, j) for j in range(len(grid)) for i in range(len(grid[0])) if grid[j][i] == "^"][0]
    direction = directions[direction_index]
    numberOfObstructions = sum([line.count("#") for line in grid])
    numberOfCollisions = 0 # For part 2
    while inBounds(position[0], position[1]) and numberOfCollisions <= numberOfObstructions:
        grid_temp[position[1]][position[0]] = "X"
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if inBounds(new_position[0], new_position[1]) and grid[new_position[1]][new_position[0]] == '#':
            numberOfCollisions += 1
            direction_index = (direction_index + 1) % 4  # Corresponds to a turn to the right
            direction = directions[direction_index]
        else:
            position = new_position
    if output_result:
        print(sum([line.count("X") for line in grid_temp]))
    return inBounds(position[0], position[1])
def part_2():
    # x is first component, y is second component, +x is right, +y is down
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_index = 3  # directions[direction_index] represents the current direction of travel
    position = [(i, j) for j in range(len(grid)) for i in range(len(grid[0])) if grid[j][i] == "^"][0]
    direction = directions[direction_index]
    numberOfObstructions = sum([line.count("#") for line in grid])
    potential_positions = []
    result = 0
    while inBounds(position[0], position[1]):
        pretend_direction_index = (direction_index + 1) % 4
        pretend_direction = directions[pretend_direction_index]
        # Check if there is an obstruction directly to the right of us.
        hasObstruction = any([grid[position[1] + (i * pretend_direction[1])][position[0] + (i * pretend_direction[0])] == "#"
                          for i in range(max([len(grid), len(grid[0])]))
                          if inBounds(position[0] + (i * pretend_direction[0]), position[1] + (i * pretend_direction[1]))])
        new_position = (position[0] + direction[0], position[1] + direction[1])
        # We will create a list of potential positions
        if inBounds(new_position[0], new_position[1]) and grid[new_position[1]][new_position[0]] == '#':
            direction_index = (direction_index + 1) % 4  # Corresponds to a turn to the right
            direction = directions[direction_index]
        else:
            if inBounds(new_position[0], new_position[1]) and hasObstruction:
                potential_positions.append(new_position)
            position = new_position
    potential_positions = list(set(potential_positions))
    for potential_position in potential_positions:
        pretend_grid = [line.copy() for line in grid]
        pretend_grid[potential_position[1]][potential_position[0]] = "#"
        if part_1(pretend_grid):
            result += 1
    print(result)

part_1(grid, output_result=True)
part_2()