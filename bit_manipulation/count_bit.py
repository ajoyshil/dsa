# Given an integer n, return an array ans of length n + 1
# such that for each i (0 <= i <= n), ans[i] is the number of
# 1's in the binary representation of i.

"""
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""
def count_bit(n):
    res = []
    for i in range(n+1):
        num = i
        count = 0
        while i!=0:
            count += 1
            i = i & i-1
        res.append({num: count})
    return res


print(count_bit(5))
