
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray, n: int) -> int:
    # Initialize the count of submatrices with n numbers to 0
    count = 0
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to n
            if matrix[i, j] == n:
                # Increment the count of submatrices with n numbers
                count += 1

    # Return the count of submatrices with n numbers
    return count
