
def dups(nums):
    result = []

    for i in range(len(nums)):
        index = abs(nums[i]) - 1

        if nums[index] < 0:
            result.append(abs(nums[i]))
        else:
            nums[index] = -nums[index]

    return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(dups(nums))
