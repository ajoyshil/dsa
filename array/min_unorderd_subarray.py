def solve(arr):
    # min_num = 9999999999
    # max_num = -9999999999
    # n = len(A)
    # for i in A:
    #     min_num = min(i, min_num)
    #     max_num = max(i, max_num)
    # l, r = 0, n-1
    # for i in range(int(n/2)):
    #     if A[i] < min_num and A[r] > max_num and min_num < max_num:
    #         return r-l+1
    #     else:
    #         if A[i] >= min_num and :
    #             l += 1
    #             min_num = A[i]
    #         if A[r] <= max_num and min_num < max_num:
    #             r -= 1
    #             max_num = A[r]
    A = arr.copy()
    B = arr
    B.sort()
    n = len(A)
    l, r = 0, n - 1

    for i in range(n):
        if A[i] == B[i]:
            l += 1
        else:
            break

    for i in range(n - 1, 0, -1):
        if A[i] == B[i]:
            r -= 1
        else:
            break
    return r - l + 1
    # return r-l+1


arr = [1, 2, 5, 3, 4, 6, 7, 8]
a = solve(arr)
# print(a)


def solve_min_diff(A, B):
    n = len(A)
    A.sort()
    if n >= B:
        min_diff = A[B - 1] - A[0]
    else:
        return -1

    for i in range(B, n):
        diff = A[i] - A[i-B+1]
        min_diff = min(diff, min_diff)
    return min_diff


arr2 = [7, 2, 4, 5, 6]
s = solve_min_diff(arr2, 3)
print(s)
