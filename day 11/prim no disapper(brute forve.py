
def disappear_nos(nums):
    result = []
    n = len(nums)

    for n in range(1, n + 1):
        if n not in nums:
            result.append(n)

    return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(disappear_nos(nums))
