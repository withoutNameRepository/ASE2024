from typing import List


def identical_elements(l1: List[object], l2: List[object]) -> set[object]:
    result = []
    if not l1 or not l2:
        return set(result)
    sliced_l1 = l1[27:55 + 1]
    sliced_l2 = l2[27:55 + 1]
    for i in sliced_l1:
        if i in sliced_l2:
            sliced_l2.remove(i)
            result.append(i)

    return set(result)