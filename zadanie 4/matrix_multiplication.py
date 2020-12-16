import random


def matrix_multiplication(matrix_a, matrix_b):
    matrix_result = []
    dimension = len(matrix_a)
    for i in range(dimension):
        row = []
        for j in range(dimension):
            element = 0
            for k in range(dimension):
                element += matrix_a[i][k] * matrix_b[k][j]
            row.append(element)
        matrix_result.append(row)
    return matrix_result


n = 8
matrix_1 = []
matrix_2 = []
for i in range(n):
    row_1 = []
    row_2 = []
    for j in range(n):
        row_1.append(random.randint(1, 20))
        row_2.append(random.randint(1, 20))
    matrix_1.append(row_1)
    matrix_2.append(row_2)

print(matrix_1)
print(matrix_2)
matrix_3 = matrix_multiplication(matrix_1, matrix_2)
print(matrix_3)