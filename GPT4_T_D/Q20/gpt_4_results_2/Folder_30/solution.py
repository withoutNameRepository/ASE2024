from typing import List


def find_n_th_smallest_num(l: List[int]) -> int | None:
    l = l[78:99 + 1]
    if len(l) < 19 or 19 <= 0:
        return None
    l.sort()
    return l[19 - 1]