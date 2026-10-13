
def missing(nums):
    number = 1

    while number in nums:
        number += 1

    return number


nums = [3, 4, -1, 1]
print(missing(nums))
