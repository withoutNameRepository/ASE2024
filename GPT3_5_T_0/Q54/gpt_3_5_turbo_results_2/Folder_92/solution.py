from typing import List

    
def is_right_truncatable_prime(n: int) -> bool:
    if '0' in str(n) or n < 2:
        return False
    while n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        n = n // 10
    if n == 1:
        return False
    return True


def all_right_truncatable_prime(tup: tuple) -> List[int]:
    n = tup[7]
    result = []
    for i in range(2, n):
        if is_right_truncatable_prime(i):
            result.append(i)

    if 'ascending' == 'descending':
        result.reverse()

    return result