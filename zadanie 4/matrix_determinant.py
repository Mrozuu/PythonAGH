import random
import numpy


def determinant(matrix):
    result = 0
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if len(matrix) == 1:
        return matrix[0][0]

    for i in list(range(len(matrix))):
        matrix_copy = matrix.copy()
        matrix_copy = matrix_copy[1:]

        for j in range(len(matrix_copy)):
            matrix_copy[j] = matrix_copy[j][0:i] + matrix_copy[j][i+1:]

        sign = (-1) ** (i % 2)
        s_det = determinant(matrix_copy)
        result += sign * matrix[0][i] * s_det

    return result


dimension = 8
matrix_1 = []
for i in range(dimension):
    row = []
    for j in range(dimension):
        row.append(random.randint(1, 20))
    matrix_1.append(row)

print(matrix_1)
print(determinant(matrix_1))
