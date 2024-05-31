
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the specified range of the input list
    for i in range(5, 8):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the positive integer to the output list
            pos_ints.append(my_list[i])
    # Return the output list of positive integers
    return pos_ints
