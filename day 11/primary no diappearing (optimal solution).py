
def disappear_nos(nums):
    n = len(nums)

    # marking the numbers present in the array by negating the value at their corresponding index
    for i in range(n):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])

    # finding the nummbers whose postions remmmain postive 
    result = []

    for i in range(n):
        if nums[i] > 0:
            result.append(i + 1)

    return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(disappear_nos(nums))
