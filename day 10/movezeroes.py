def moveZeroes(nums):
    write = 0

    # Step 1: Shift all non-zero numbers to the front
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    # Step 2: Fill the rest of the array with zeroes
    while write < len(nums):
        nums[write] = 0
        write += 1