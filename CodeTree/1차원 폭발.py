n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# check sequence numbers
def is_continuous(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i + 1]:
            d = i + 1
            while d < len(nums) and nums[i] == nums[d]:
                d += 1
            if d - i >= m:
                return True
    return False


# boom sequence numbers
def boom(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            num = nums[i]
            d = i + 1
            while d < len(nums) and num == nums[d]:
                d += 1
            if d - i >= m:
                for x in range(i, d):
                    nums[x] = 0
            i = d
        else:
            i += 1


# apply gravity
def gravity(nums):
    temp = []
    temp_i = 0
    for elem in nums:
        if elem == 0:
            continue
        else:
            temp.append(elem)
            temp_i += 1

    return temp



if m == 1:
    print(0)
else:
    while is_continuous(numbers):
        boom(numbers)
        numbers[:] = gravity(numbers)

    print(len(numbers))
    for element in numbers:
        print(element)
