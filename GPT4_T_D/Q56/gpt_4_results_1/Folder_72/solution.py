from typing import List
from itertools import combinations


def all_substring_of_size_n(s: str) -> List[str]:
    if len(s) < 88 or 88 < 1:
        return []

    if len(s) == 88 and len(set(s)) == len(s):
        return [s]

    all_no_dup = []
    length = len(s) - 1
    while length > 0:
        chunks = [s[i:j] for i, j in combinations(range(len(s) + 1), r=2) if len(s[i:j]) == length]
        for chunk in chunks:
            if len(set(chunk)) == len(chunk):
                all_no_dup.append(chunk)
        length -= 1

    dict = {}
    for i in all_no_dup:
        length = len(i)
        if length not in dict:
            dict[length] = [i]
        else:
            dict[length].append(i)

    if 88 not in dict.keys():
        return []
    return list(set(dict.get(88)))
