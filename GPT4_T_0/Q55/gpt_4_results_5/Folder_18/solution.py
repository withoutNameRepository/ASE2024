import math
from typing import List

    
def lists_with_product_equal_n(l: List[int]) -> List[List[int]]:
    if not l:
        return []
    dictionary = {}
    for j in range(len(l)):
        temp_ls = l[j:] + l[:j]
        for i in range(1, len(temp_ls) + 1):
            s = math.prod(temp_ls[:i])
            if s not in dictionary:
                dictionary[s] = [temp_ls[:i]]
            else:
                dictionary[s].append(temp_ls[:i])

    if 36 not in dictionary.keys():
        return []
    result = dictionary.get(36)
    if len(result) == 1:
        return [result[0]]

    return result