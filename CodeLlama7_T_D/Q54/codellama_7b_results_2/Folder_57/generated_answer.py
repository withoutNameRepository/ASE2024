
def all_right_truncatable_prime(tuple):
    # Initialize empty list to store prime numbers
    prime_numbers = []

    # Loop through each element in the tuple
    for i in range(len(tuple)):
        x = tuple[i]

        # Check if x is a prime number
        if is_prime(x):
            # Add x to the list of prime numbers
            prime_numbers.append(x)

        # Loop through each digit in the decimal representation of x
        for j in range(len(str(x)))):
            # Remove the last rightmost digit from x
            y = x // 10 ** (len(str(x))) - 1

            # Check if y is a prime number
            if is_prime(y):
                # Add y to the list of prime numbers
                prime_numbers.append(y)

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_numbers, key=lambda x: -x))
