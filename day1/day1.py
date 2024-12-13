def part_1():
    input_text = open("input.txt").readlines()
    data = [line.split("   ") for line in input_text]
    list_1 = [int(d[0]) for d in data]
    list_2 = [int(d[1]) for d in data]
    list_1.sort()
    list_2.sort()
    sum = 0
    for i in range(len(list_1)):
        sum += abs(list_2[i] - list_1[i])
    print(sum)
def part_2():
    input_text = open("input.txt").readlines()
    data = [line.split("   ") for line in input_text]
    list_1 = [int(d[0]) for d in data]
    list_2 = [int(d[1]) for d in data]
    sum = 0
    for d in list_1:
        sum += d * list_2.count(d)
    print(sum)

part_1()
part_2()