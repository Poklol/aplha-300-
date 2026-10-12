
def twosum(no, target):
    for i in range(len(no)):
        for j in range(i + 1, len(no)):
            if no[i] + no[j] == target:
                return [i, j]

    return []

no = [2, 7, 11, 15]
target = 9

result = twosum(no, target)
print(result)
