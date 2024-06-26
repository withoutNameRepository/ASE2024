
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")

    # Check if the list is empty

    if len(my_list) == 0:
        return None

    # Get the smallest element in the list

    smallest = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]

    # Check if there is a second smallest element

    second_smallest = None

    for i in range(56, 83):
        if my_list[i] != smallest:
            second_smallest = my_list[i]
            break

    return second_smallest
