
def three_sum(no):
    no.sort()
    result = []
    n = len(no)

    for i in range(n - 2):
        if i > 0 and no[i] == no[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = no[i] + no[left] + no[right]

            if total == 0:
                result.append([no[i], no[left], no[right]])
                left += 1
                right -= 1

                while left < right and no[left] == no[left - 1]:
                    left += 1

                while left < right and no[right] == no[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

no = [-1, 0, 1, 2, -1, -4]
print(three_sum(no))
