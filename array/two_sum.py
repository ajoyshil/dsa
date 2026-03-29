
# Two Sum

# Input: nums = [2, 7, 11, 15], target = 9  
# Output: [0, 1]

# Input: nums = [3, 2, 4], target = 6  
# Output: [1, 2]


# considering array is sorted 

def twosum(num, target):
    num = sorted(num)
    l,r = 0, len(num)-1
    current_sum = 0
    while l < r:
        current_sum = num[l] + num[r]
        if current_sum == target:
            return (l,r)
        if current_sum > target:
            r -= 1
        elif current_sum < target:
            l += 1
    return (-1, -1)

nums = [2, 7, 11, 15]
target = 9  

print(twosum(nums, target))

# Time Complexicity = O(n)
# Space Complexicity = O(1)