def sortArrayByParity(nums):
    write = 0

    for read in range(len(nums)):
        # Check if the number is even
        if nums[read] % 2 == 0:
            # Swap so we don't overwrite odd numbers; just push them back
            nums[write], nums[read] = nums[read], nums[write]
            write += 1

    return nums