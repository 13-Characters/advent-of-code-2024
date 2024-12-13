import re
def part_1():
    input = "".join(open("input.txt").readlines())
    instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)
    result = 0
    for instruction in instructions:
        num_1, num_2 = instruction.removeprefix("mul(").removesuffix(")").split(",")
        num_1, num_2 = int(num_1), int(num_2)
        result += num_1 * num_2
    print(result)
def part_2():
    input = "".join(open("input.txt").readlines())
    result = 0
    segments = input.split("do()")
    for segment in segments:
        stop = segment.find("don't()")
        if stop != -1:
            segment = segment[:stop]
        instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', segment)
        for instruction in instructions:
            num_1, num_2 = instruction.removeprefix("mul(").removesuffix(")").split(",")
            num_1, num_2 = int(num_1), int(num_2)
            result += num_1 * num_2
    print(result)

part_1()
part_2()