def spiral(arr):
    row_start = 0
    row_end = len(arr) - 1
    col_start = 0
    col_end = len(arr[0]) - 1
    res = []
    while row_start <= row_end and col_start <= col_end:
        # 1 st row
        for i in range(col_start, col_end + 1):
            res.append(arr[row_start][i])
        row_start = row_start + 1
        # last column
        for i in range(row_start, row_end + 1):
            res.append(arr[i][col_end])
        col_end = col_end - 1
        # last row
        for i in range(col_end, col_start - 1, -1):
            res.append(arr[row_end][i])
        row_end = row_end - 1
        # first column
        for i in range(row_end, col_start, -1):
            res.append(arr[i][col_start])
        col_start = col_start + 1

    print(res)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrix2 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

matrix3 = [[1, 2, 3, 10],
          [4, 5, 6, 11],
          [7, 8, 9, 12],
          [13,14,15,16]]

spiral(matrix3)
