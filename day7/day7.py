input = open("input.txt").readlines()
def part_1():
    answer = 0
    for line in input:
        test_value, nums = line.split(": ")
        test_value = int(test_value)
        nums = nums.split(" ")
        nums = [int(num) for num in nums]
        for i in range(2 ** (len(nums) - 1)):
            result = nums[0]
            for j in range(len(nums) - 1):
                if (i & 2 ** j) != 0:
                    result += nums[j + 1]
                else:
                    result *= nums[j + 1]
            if result == test_value:
                answer += test_value
                break
    print(answer)
def part_2():
    def toBase3(num, length):
        result = ""
        digits = ["0", "1", "2"]
        for i in range(length):
            result = digits[num % 3] + result
            num = num // 3
        return result
    answer = 0
    for line in input:
        test_value, nums = line.split(": ")
        test_value = int(test_value)
        nums = nums.split(" ")
        nums = [int(num) for num in nums]
        for i in range(3 ** (len(nums) - 1)):
            result = nums[0]
            baseThree = toBase3(i, len(nums) - 1)
            for j in range(len(nums) - 1):
                if baseThree[j] == "0":
                    result += nums[j + 1]
                elif baseThree[j] == "1":
                    result *= nums[j + 1]
                else:
                    result = int(str(result) + str(nums[j + 1]))
            if result == test_value:
                answer += test_value
                break
    print(answer)

part_1()
part_2()