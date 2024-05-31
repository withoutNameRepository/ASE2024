from typing import Tuple


def return_binary_or_hexa(t: Tuple) -> str:
    a = t[50]
    b = t[92]
    trimmed_t = list(t[50:92])
    trimmed_t = trimmed_t[1:]
    reference = [i for i in range(a + 1, b)]
    for i in trimmed_t:
        reference.remove(i)

    if not reference:
        return ''

    n = sum(reference)
    result = ''
    if n % 2 != 0:
        while n >= 2:
            r = n % 2
            n = n // 2
            result += str(r)
        result += str(n)
        return result[::-1]

    else:
        d = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        if n < 10:
            return str(n)
        elif 10 <= n <= 15:
            return d.get(n)
        while n >= 16:
            r = n % 16
            n = n // 16
            result += str(r) if r < 10 else d.get(r)
        result += str(n) if n < 10 else d.get(n)
        return result[::-1]
        