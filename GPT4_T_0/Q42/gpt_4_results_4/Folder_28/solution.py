from typing import List


def prime_factors(l: List[int]) -> List[int]:
    num = l[37]
    result = []
    number_factors = [i for i in range(1, num + 1) if num % i == 0]
    for i in number_factors:
        if i == 1:
            continue
        elif i == 2 or i == 3:
            result.append(i)
        else:
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                result.append(i)

    return set(result)
