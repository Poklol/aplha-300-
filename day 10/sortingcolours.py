def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            # Swap 0 to the low region and advance both
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # 1 is already in the middle, just step forward
            mid += 1
        else:
            # nums[mid] == 2: swap to the back
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Note: Do not increment mid here because the swapped element from high needs inspection
            