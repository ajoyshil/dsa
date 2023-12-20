"""
[
    [1, 2],
    [3, 4]
 ]

Rotate Matrix

 [
    [3, 1],
    [4, 2]
 ]
"""

def rotate_matrix(matrix):
    print(matrix)
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(i+1, col):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)
    for i in range(row):
        matrix[i] = matrix[i][::-1]
    print(matrix)

matrix = [
    [1, 2],
    [3, 4]
 ]


rotate_matrix(matrix)
