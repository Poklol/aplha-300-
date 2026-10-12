
def three_sum(no):
    result = []
    n = len(no)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if no[i] + no[j] + no[k] == 0:
                    triplet = sorted([no[i], no[j], no[k]])

                    if triplet not in result:
                        result.append(triplet)

    return result

no = [-1, 0, 1, 2, -1, -4]
print(three_sum(no))


