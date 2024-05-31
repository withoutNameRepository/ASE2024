from typing import List


def gcf_two_nums(l: List[int]) -> int | None:
    if len(l) < 2:
        return None
    x, y = l[17], l[20]
    x_factors = [i for i in range(1, x + 1) if x % i == 0]
    y_factors = [i for i in range(1, y + 1) if y % i == 0]

    result = 0
    for i in reversed(x_factors):
        if i in y_factors:
            result = i
            break
    return result