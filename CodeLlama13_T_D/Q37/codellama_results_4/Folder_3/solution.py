def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[37:56 + 1]
    for char in sliced_s:
        if '6' <= char <= '_':
            s = s.replace(char, '')

    return s