from typing import List


def find_divisors_in_range(n: int) -> List[int]:
    x, y = 32, 90
    if y < 1 or n < x:
        return []
    if x < 1:
        x = 1
    if n < y:
        y = n
    return [i for i in range(x, y + 1) if n % i == 0]
    