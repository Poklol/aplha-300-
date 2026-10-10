def removeElement(nums, val):
    write = 0

    for read in range(len(nums)):
        # Keep everything that is NOT equal to val
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1

    return write