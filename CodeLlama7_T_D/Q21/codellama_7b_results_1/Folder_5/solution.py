from typing import List


def all_ints_div_by_num(l: List[int]) -> List[int]:
    l = l[1:4 + 1]
    return [i for i in l if i % -6 == 0]
