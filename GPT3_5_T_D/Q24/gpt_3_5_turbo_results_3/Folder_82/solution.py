def sum_of_divisors_in_range(n: int) -> int:
    x, y = 4, 6
    if y < 1 or n < x:
        return 0
    if x < 1:
        x = 1
    if n < y:
        y = n
    return sum([i for i in range(x, y + 1) if n % i == 0])