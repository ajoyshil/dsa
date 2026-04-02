""""
Trapping Rain Water

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
"""
from typing import List


def trap(height: List[int]) -> int:
    l ,r = 0, len(height ) -1
    lm = height[l]
    rm = height[r]
    res = 0
    while l <= r:

        if lm <= rm:
            lm = max(lm, height[l])
            res = res + lm - height[l]
            l += 1
        else:
            rm = max(rm, height[r])
            res = res + rm - height[r]
            r -= 1
    return res

arr = [5,5,1,7,1,1,5,2,7,6]

res = trap(arr)

print(res)