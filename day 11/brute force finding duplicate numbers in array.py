
def dups(nums):
    result = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and nums[i] not in result:
                result.append(nums[i])

    return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(dups(nums))
