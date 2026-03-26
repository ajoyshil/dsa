

player = [
    [0,1,2,2,0],
    [0,1,0,2,0],
    [0,1,0,1,2],
    [0,0,0,1,0],
    [1,1,1,0,0]
]

def calculate_win_probability(arr):
    m = 0
    for i in range(len(arr)):
        s = 0

        for j in range(len(arr[0])):
            if arr[i][j] == 1 or arr[i][j] == 2:
                s += 1
                m = max(m, s)
                arr[i][j] = s
            else:
                arr[i][j] = s
    res = []
    for i in range(len(arr)):
        if arr[i][-1] >= m:
            res.append(1)
        else:
            res.append(0)
    return res


print(calculate_win_probability(player))
