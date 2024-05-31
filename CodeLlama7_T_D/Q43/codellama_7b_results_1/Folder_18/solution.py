from typing import List


def find_primes_between_indices(l: List[int]) -> List[int]:
    result = []
    if not l:
        return result
    flag = False
    sliced_l = l[328:668 + 1]
    for i in sliced_l:
        if i <= 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if flag:
            flag = False
        else:
            result.append(i)
    
    if "descending" == "descending":
        return sorted(result, reverse=True)
    else:
        return sorted(result)
        