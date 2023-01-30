def search(A, B):
    l, r = 0, len(A) - 1
    while l <= r:
        m = int((l + r) / 2)
        if B == A[m]:
            return m
        if B >= A[0] : #  rotated part
            if A[0] > A[m]:
                r = m -1
            else:
                if B < A[m]:
                    r = m - 1
                else:
                    l = m + 1
        else: # non rotated part
            if A[0] <= A[m]:
                l = m+1
            else:
                if B > A[m]:
                    l = m + 1
                else:
                    r = m - 1
    return -1


A = [ 5, 6, 1, 2, 3 ]
B = 3

print(search(A, B))
