def return_binary_or_hexa(test_tup):
    res = test_tup[35] + 1
    res += test_tup[test_tup.index(max(test_tup)) - 1] - test_tup[test_tup.index(min(test_tup)) - 1]
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
