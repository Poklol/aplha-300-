def twosum(no, target):
    seen = {}

    for i in range(len(no)):
        needed = target - no[i]

        if needed in seen:
            return [seen[needed], i]

        seen[no[i]] = i

    return []

no = [2, 7, 11, 15]
target = 9

result = twosum(no, target)
print(result)
