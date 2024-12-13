import string
def part_1():
    input = "".join(open("input.txt").readlines())
    result = 0
    pos = 0
    while True:
        pos = input.find("mul", pos)
        if pos == -1:
            break
        left = input.find("(", pos)
        right = input.find(")", pos)
        if left == (pos + 3) and "," in input[left+1:right] and len(input[left+1:right].split(",")) == 2:
            num_1, num_2 = input[left+1:right].split(",")
            if all([digit in string.digits for digit in num_1]) and all([digit in string.digits for digit in num_2]):
                result += int(num_1) * int(num_2)
        pos += 1
    print(result)
def part_2():
    input = "".join(open("input.txt").readlines())
    result = 0
    segments = input.split("do()")
    for segment in segments:
        pos = 0
        stop = segment.find("don't()")
        if stop != -1:
            segment = segment[:stop]
        while True:
            pos = segment.find("mul", pos)
            if pos == -1:
                break
            left = segment.find("(", pos)
            right = segment.find(")", pos)
            if (left == pos+3) and "," in segment[left:right] and len(segment[left+1:right].split(",")) == 2:
                num_1, num_2 = segment[left+1:right].split(",")
                if all([digit in string.digits for digit in num_1]) and all(
                        [digit in string.digits for digit in num_2]):
                    result += int(num_1) * int(num_2)
            pos += 1
    print(result)

part_1()
part_2()