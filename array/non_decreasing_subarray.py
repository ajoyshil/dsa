def solve(A, B):
    n = len(A)
    pf = [0] * n
    dp = [0] * n
    dp[0] = 0
    ans = []
    for i in range(1, n):
        if A[i] < A[i - 1]:
            dp[i] = 1
    pf[0] = dp[0]
    for i in range(n):
        pf[i] = pf[i - 1] + dp[i]

    for i in range(len(B)):
        v = pf[B[i][1] - 1] - pf[B[i][0] - 1]
        # v = B[i][1]
        # print(v)
        if v > 0:
            ans.append(1)
        else:
            ans.append(0)
    return ans


A = [ 7, 7, 1, 6, 9 ]
B = [[1, 3], [4, 5], [1, 2], [3, 4], [1, 5]]

res = solve(A, B)
print(res)
