import string
from itertools import permutations


def palindromes_between_indices(s: str) -> set[str]:
    s = s[6: 8 + 1]
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.translate(str.maketrans('', '', string.digits))
    s = s.replace(' ', '')
    if len(s) < 3 or len(list(s)) == len(set(s)):
        return set()
    all_palindrome = set()
    result = []
    if len(s) < 3:
        return all_palindrome
    for i in range(3, len(s) + 1):
        result += (list(permutations(s, i)))

    return {''.join(i) for i in result if ''.join(i).lower() == ''.join(i).lower()[::-1]}