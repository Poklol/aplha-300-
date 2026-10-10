def removeDuplicatesII(nums):
    # If the list has 2 or fewer elements, all are allowed
    if len(nums) <= 2:
        return len(nums)

    # First two elements are always accepted
    write = 2

    for read in range(2, len(nums)):
        # Compare with the item placed two slots back in the clean prefix
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    return write