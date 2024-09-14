def interchange_columns(matrix):
    rows = len(matrix)
    for i in range(rows):
        matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
    return matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = interchange_columns(matrix)
print("Matrix after interchanging first and last columns:")
for row in result:
    print(row)