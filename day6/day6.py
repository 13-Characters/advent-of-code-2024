import renderer
from PIL import Image
grid = [list(line.removesuffix("\n")) for line in open("input.txt").readlines()]
def renderGrid(grid, output_name):
    grid_image = Image.new("RGBA", (len(grid[0]), len(grid)))
    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            if point == "#":
                grid_image.putpixel((x, y), (226, 88, 79, 255))
            elif point == "^":
                grid_image.putpixel((x, y), (255, 212, 187, 255))
            elif point == "!":
                grid_image.putpixel((x,y), (255, 0, 0, 255))
            elif point == "@":
                grid_image.putpixel((x,y), (255, 255, 255, 255))
            else:
                grid_image.putpixel((x,y), (123, 205, 237, 255))
    grid_image.save(f"frames/{output_name}.png")
    renderer.renderFrame(f"frames/{output_name}.png")
    return grid_image

def inBounds(x, y):
    return (0 <= x < len(grid[0])) and (0 <= y < len(grid))

grid_image = renderGrid(grid, "grid")
def part_1():
    grid_temp = [line.copy() for line in grid]
    # x is first component, y is second component, +x is right, +y is down
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_index = 3  # directions[direction_index] represents the current direction of travel
    position = [(i, j) for j in range(len(grid)) for i in range(len(grid[0])) if grid[j][i] == "^"][0]
    direction = directions[direction_index]
    while inBounds(position[0], position[1]):
        grid_temp[position[1]][position[0]] = "X"
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if inBounds(new_position[0], new_position[1]) and grid[new_position[1]][new_position[0]] == '#':
            direction_index = (direction_index + 1) % 4  # Corresponds to a turn to the right
            direction = directions[direction_index]
        else:
            position = new_position
    print(sum([line.count("X") for line in grid_temp]))
def part_2():
    # x is first component, y is second component, +x is right, +y is down
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_index = 3  # directions[direction_index] represents the current direction of travel
    position = [(i, j) for j in range(len(grid)) for i in range(len(grid[0])) if grid[j][i] == "^"][0]
    og_position = position
    direction = directions[direction_index]
    numberOfObstructions = sum([line.count("#") for line in grid])
    validPositions = []
    while inBounds(position[0], position[1]):
        grid[position[1]][position[0]] = "^"
        pretend_direction_index = (direction_index + 1) % 4
        pretend_direction = directions[pretend_direction_index]
        # Check if there is an obstruction directly to the right of us.
        hasObstruction = any([grid[position[1] + (i * pretend_direction[1])][position[0] + (i * pretend_direction[0])] == "#"
                          for i in range(max([len(grid), len(grid[0])]))
                          if inBounds(position[0] + (i * pretend_direction[0]), position[1] + (i * pretend_direction[1]))])
        # If there is an obstruction to the right of us, pretend there is an obstruction right in front of us and see what happens
        if hasObstruction:
            # While we are pretending that there is an obstruction right in front of us, count the number of collisions.
            # If it is greater than the number of obstructions on the grid, we stop because we can be certain that we are in a loop.
            numberOfCollisions = 0
            pretend_direction_index = direction_index
            pretend_direction = directions[pretend_direction_index]
            pretend_position = position
            pretend_grid = [line.copy() for line in grid]
            if inBounds(position[0] + direction[0], position[1] + direction[1]):
                pretend_grid[position[1] + direction[1]][position[0] + direction[0]] = "#"
                while inBounds(pretend_position[0], pretend_position[1]) and (numberOfCollisions <= numberOfObstructions):
                    pretend_grid[pretend_position[1]][pretend_position[0]] = "^"
                    new_pretend_position = (pretend_position[0] + pretend_direction[0], pretend_position[1] + pretend_direction[1])
                    if inBounds(new_pretend_position[0], new_pretend_position[1]) and pretend_grid[new_pretend_position[1]][new_pretend_position[0]] == "#":
                        pretend_direction_index = (pretend_direction_index + 1) % 4
                        pretend_direction = directions[pretend_direction_index]
                        numberOfCollisions += 1
                    else:
                        pretend_position = new_pretend_position
                if inBounds(pretend_position[0], pretend_position[1]):
                    # We have found a valid position for our obstruction. Now, add one to our answer
                    validPositions.append((position[0] + direction[0], position[1] + direction[1]))
                    pretend_grid[position[1] + direction[1]][position[0] + direction[0]] = "!"
                    pretend_grid[og_position[1]][og_position[0]] = "@"
                    renderGrid(pretend_grid, str(len(validPositions)))

        new_position = (position[0] + direction[0], position[1] + direction[1])
        if inBounds(new_position[0], new_position[1]) and grid[new_position[1]][new_position[0]] == '#':
            direction_index = (direction_index + 1) % 4  # Corresponds to a turn to the right
            direction = directions[direction_index]
        else:
            position = new_position
    print(len(set(validPositions)))

part_1()
part_2()