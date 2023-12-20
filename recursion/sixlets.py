"""
Problem Description
Given a array of integers A of size N and an integer B.

Return number of non-empty subsequences of A of size B having sum <= 1000.
A = [5, 17, 1000, 11]
B = 4
"""

A = [1, 2, 8]
B = 2

# A = [5, 17, 1000, 11]
# B = 4

def solve(A, B):

    return find_sixlet(A,B, 0, 0)

def find_sixlet(A, n,i, s):
    if s > 1000:
        return 0
    if n == 0:
        return 1
    if i == len(A):
        return 0
    return find_sixlet(A, n, i+1, s) + find_sixlet(A, n-1, i+1, s+A[i])

print(solve(A, B))