import string
grid = [list(line.removesuffix("\n")) for line in open("input.txt").readlines()]
def get_antinodes(coord_list, grid_dimensions, part_1=True):
    antinodes_list = []
    width = grid_dimensions[0]
    height = grid_dimensions[1]
    for i, first_coord in enumerate(coord_list):
        for second_coord in coord_list[i+1:]:
            dx = second_coord[0] - first_coord[0]
            dy = second_coord[1] - first_coord[1]
            count = 1
            while ((0 <= second_coord[0] + count*dx < width and 0 <= second_coord[1] + count*dy < height)
                   and ((part_1 and count < 2) or not part_1)):
                antinodes_list.append((second_coord[0] + count*dx, second_coord[1] + count*dy))
                count += 1
            count = 1
            while ((0 <= first_coord[0] - count*dx < width and 0 <= first_coord[1] - count*dy < height)
                   and ((part_1 and count < 2) or not part_1)):
                antinodes_list.append((first_coord[0] - count*dx, first_coord[1] - count*dy))
                count += 1
    if not part_1:
        antinodes_list = antinodes_list + coord_list
    return antinodes_list

def part_1():
    alphanumeric = string.digits + string.ascii_letters
    antenna_positions = {} # Dictionary with the key being a specific frequency and value being the coords of all antennas tuned to that frequency
    antinodes = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] not in antenna_positions.keys() and grid[y][x] in alphanumeric:
                antenna_positions[grid[y][x]] = [(x, y)]
            else:
                if grid[y][x] in alphanumeric:
                    antenna_positions[grid[y][x]].append((x, y))
    for frequency in antenna_positions.keys():
        antinodes = antinodes | set(get_antinodes(antenna_positions[frequency], (len(grid[0]), len(grid)), part_1=True))
    print(len(antinodes))
def part_2():
    alphanumeric = string.digits + string.ascii_letters
    antenna_positions = {}  # Dictionary with the key being a specific frequency and value being the coords of all antennas tuned to that frequency
    antinodes = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] not in antenna_positions.keys() and grid[y][x] in alphanumeric:
                antenna_positions[grid[y][x]] = [(x, y)]
            else:
                if grid[y][x] in alphanumeric:
                    antenna_positions[grid[y][x]].append((x, y))
    for frequency in antenna_positions.keys():
        antinodes = antinodes | set(get_antinodes(antenna_positions[frequency], (len(grid[0]), len(grid)), part_1=False))
    print(len(antinodes))
part_1()
part_2()