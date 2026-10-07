def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    counts = {}
    for x in nums1:
        counts[x] = counts.get(x, 0) + 1
        
    res = []
    for x in nums2:
        if counts.get(x, 0) > 0:
            res.append(x)
            counts[x] -= 1
    return res