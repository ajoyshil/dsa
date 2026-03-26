def sub_array(arr):
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            print(current_sum)


arr = [1, 3, -4, 6, 8, 0, -2]
sub_array(arr)

# find the sum of all sub array
"""
using contribution of every element in all sub array
"""

def total_sum(A):
    sum = 0
    for i in range(len(A)):
        left = i+1
        right = len(A)-i
        total = left*right
        sum += total * A[i]
    return sum


print(total_sum([1,2, -2]))


