
def filter_chars(string):
    filtered_string = ""
    for i in range(1, len(string)):
        if string[i] >= 'L' and string[i] <= 'a':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
