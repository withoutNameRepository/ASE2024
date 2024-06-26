
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci number that occurs at the 144th position in the sequence
    fibonacci_number = 0
    for i in range(144):
        fibonacci_number = (fibonacci_number + fibonacci_number[i - 1]) % 100000000
    # Check if the decimal integer is divisible by the Fibonacci number
    return decimal_integer % fibonacci_number == 0
