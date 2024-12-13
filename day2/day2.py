def isMonotone(list):
    sorted_list = sorted(list)
    return sorted_list == list or sorted_list[::-1] == list
def part_1_old():
    lines = open("input.txt").readlines()
    count = 0
    for line in lines:
        line = line.removeprefix("\n")
        nums = line.split(" ")
        nums = [int(num) for num in nums]
        if not isMonotone(nums):
            continue
        diffs_criteria = [1 <= abs(right - left) <= 3 for left, right in zip(nums[:-1], nums[1:])]
        if all(diffs_criteria):
            count += 1
    print(count)
def part_1():
    lines = open("input.txt").readlines()
    count = 0
    for line in lines:
        line = line.removeprefix("\n")
        nums = line.split(" ")
        nums = [int(num) for num in nums]
        diffs = [right - left for left, right in zip(nums[:-1], nums[1:])]
        if all([1 <= diff <= 3 for diff in diffs]) or all([-3 <= diff <= -1 for diff in diffs]):
            count += 1
    print(count)
def part_2():
    lines = open("input.txt").readlines()
    count = 0
    for line in lines:
        line = line.removeprefix("\n")
        nums = line.split(" ")
        nums = [int(num) for num in nums]
        diffs = [right - left for left, right in zip(nums[:-1], nums[1:])]
        if all([1 <= diff <= 3 for diff in diffs]) or all([-3 <= diff <= -1 for diff in diffs]):
            count += 1
        else:
            for i in range(len(nums)): # There's gotta be a better way than this
                # Make a new list that is just nums but with one element removed
                temp = nums.copy()
                temp.pop(i)
                diffs = [right - left for left, right in zip(temp[:-1], temp[1:])]
                if all([1 <= diff <= 3 for diff in diffs]) or all([-3 <= diff <= -1 for diff in diffs]):
                    count += 1
                    break
    print(count)
part_1()
part_2()