from typing import List


def if_perfect_num(l: List[int]) -> bool:
    num = l[96]
    if num <= 1:
        return False
    return sum([i for i in range(1, num) if num % i == 0]) == num