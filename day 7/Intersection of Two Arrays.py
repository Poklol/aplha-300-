def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    set1 = set(nums1)
    res = set()
    for x in nums2:
        if x in set1:
            res.add(x)
    return list(res)