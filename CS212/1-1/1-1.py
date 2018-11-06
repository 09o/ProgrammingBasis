def ss(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i] ** 2
    return total

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ss(nums))