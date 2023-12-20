"""
Rearrange Array

Given an array A of size N. Rearrange the given array so that A[i] becomes A[A[i]] with O(1) extra space.

Constraints:

1 <= N <= 5×104

0 <= A[i] <= N - 1

The elements of A are distinct

Input Format

The argument A is an array of integers

Example 1:

Input : [1, 0]
Return : [0, 1]
Example 2:

Input : [0, 2, 1, 3]
Return : [0, 1, 2, 3]
"""

def solve(A):
    n = len(A)
    for i in range(n//2):
        x = A[i]
        y = A[A[i]]
        A[i] = y
        A[A[x]] = y
        # A[i], A[A[i]] = y, x
    return A

# arr = [0, 2, 1, 3]
arr = [ 4, 0, 2, 1, 3 ]
res = solve(arr)
print(res)

s = "My name is Ajoy Shil"
s[0] = 'A'
print(s)