def part_one(nums):
    for i in nums:
        if 2020 - i in nums:
            print("num1: ", str(i), " num2: ", str(2020-i))

def part_two(nums):
    for num1 in nums:
        for num2 in nums:
            if (2020 - num1 - num2) in nums:
                print(str(num1 * num2 * (2020-num1-num2)))


with open('01.txt') as f:
    nums = [int(line) for line in f]

# part_one(nums)
part_two(nums)
