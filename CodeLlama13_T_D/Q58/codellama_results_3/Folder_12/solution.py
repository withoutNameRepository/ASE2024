import numpy as np
from typing import Any


def submatrix_with_n_numbers(mat: Any) -> int:
    result = []
    if type(mat) == list:
        if not mat:
            return []
    elif mat.size == 0:
        return []
    if type(mat).__module__ != np.__name__:
        mat = np.asmatrix(mat)
    rows, columns = mat.shape[0], mat.shape[1]
    submatrix_of_size_n = 0
    for c in range(rows):
        for i in range(columns):
            for j in range(1, columns + 1 - i):
                temp_submatrix = (mat[c:c + 1, i:i + j])
                ro, co = temp_submatrix.shape
                if ro * co == 46:
                    submatrix_of_size_n += 1

    for c in range(columns):
        for i in range(rows):
            for j in range(2, rows + 1 - i):
                temp_submatrix = (mat[i:i + j, c:c + 1])
                ro, co = temp_submatrix.shape
                if ro * co == 46:
                    submatrix_of_size_n += 1

    for i in range(0, rows - 1):
        for row in range(1, rows - i):
            for j in range(0, columns - 1):
                for column in range(1, columns - j):
                    temp_submatrix = (mat[i:row + i + 1, j:column + j + 1])
                    ro, co = temp_submatrix.shape
                    if ro * co == 46:
                        submatrix_of_size_n += 1


    return submatrix_of_size_n
