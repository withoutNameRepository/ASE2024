def if_decimal_is_divisible(binary_string: str) -> bool:
    decimal_num, j = 0, 0
    for i in range(len(binary_string) - 1, -1, -1):
        if binary_string[j] == '1':
            decimal_num += (2 ** i)
        j += 1

    f1, f2, f3, c = 0, 1, 0, 3
    while c <= 144:
        f3 = f1 + f2
        f1, f2 = f2, f3
        c += 1

    if decimal_num % f3 == 0:
        return True
    return False