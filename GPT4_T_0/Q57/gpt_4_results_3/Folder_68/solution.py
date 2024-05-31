import numpy as np
from numpy import matrix
from typing import Any, List


def submatrix_with_particular_sum(mat: Any) -> List[matrix]:
    result = []
    if type(mat) == list:
        if not mat:
            return []
    elif mat.size == 0:
        return []
    if type(mat).__module__ != np.__name__:
        mat = np.asmatrix(mat)
    rows, columns = mat.shape[0], mat.shape[1]
    for c in range(rows):
        for i in range(columns):
            for j in range(1, columns + 1 - i):
                temp_submatrix = (mat[c:c + 1, i:i + j])
                submatrix_sum = np.sum(temp_submatrix)
                if submatrix_sum == 3:
                    result.append(temp_submatrix)
    for c in range(columns):
        for i in range(rows):
            for j in range(2, rows + 1 - i):
                temp_submatrix = (mat[i:i + j, c:c + 1])
                submatrix_sum = np.sum(temp_submatrix)
                if submatrix_sum == 3:
                    result.append(temp_submatrix)
    for i in range(0, rows - 1):
        for row in range(1, rows - i):
            for j in range(0, columns - 1):
                for column in range(1, columns - j):
                    temp_submatrix = (mat[i:row + i + 1, j:column + j + 1])
                    submatrix_sum = np.sum(temp_submatrix)
                    if submatrix_sum == 3:
                        result.append(temp_submatrix)

    return result
