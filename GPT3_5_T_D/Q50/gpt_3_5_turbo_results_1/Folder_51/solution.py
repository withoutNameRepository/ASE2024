from typing import List


def if_contains_anagrams(l: List[str]) -> bool:
    if len(l) < 2:
        return False

    counter = 0
    modified_l = [x for i in l if len(x := i.replace(' ', '').lower()) > 2]

    while len(modified_l) > 1:
        x = modified_l[0]
        ll = modified_l[1:]
        for y in ll:
            if len(x) != len(y) or not x:
                continue
            if sorted(x) == sorted(y):
                counter += 1
        modified_l = modified_l[1:]

    if counter < 39:
        return False
        
    return True