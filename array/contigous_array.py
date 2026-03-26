
# @param A : list of integers
# @return an integer
def solve(A):
    n = len(A)
    for i in range(n):
        if A[i] == 0:
            A[i] = -1
    pf = [0] * n
    pf[0] = A[0]

    freq = {}
    freq[0] = -1
    ans = 0
    for i in range(1, n):
        pf[i] = pf[i - 1] + A[i]
    for i in range(n):
        if pf[i] not in freq:
            freq[pf[i]] = i
        else:
            # freq[pf[i]] -= 1
            print(pf[i], freq[pf[i]])
            ans = max(ans, i - freq[pf[i]])
    return ans


arr = [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
arr2 = [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0 ]
arr3 = [ 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1 ]

res = solve(arr3)
print(res)
