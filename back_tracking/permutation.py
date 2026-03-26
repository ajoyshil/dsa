# Problem
# Generate all permutations of a list of distinct numbers.
nums = [1, 2, 3]

# Output
# [
#   [1, 2, 3],
#   [1, 3, 2],
#   [2, 1, 3],
#   [2, 3, 1],
#   [3, 1, 2],
#   [3, 2, 1]
# ]

class Solution:
    def permute(self, nums):
        res = []
        
        def perms(i):
            if i == len(nums):
                res.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                perms(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        perms(0)
        return res
    
obj = Solution()
res = obj.permute(nums)
print(res)


# Input: nums = [2, 7, 11, 15], target = 9  
# Output: [0, 1]

# Input: nums = [3, 2, 4], target = 6  
# Output: [1, 2]

def two_sum(nums, target):
    l, r = 0, len(nums)-1
    dd = {}
    for i in range(len(nums)):
        ct = target - nums[i]
        if ct in dd:
            return [i, dd[ct]]
        dd[nums[i]] = i

res = two_sum([2, 7, 11, 15], 13)

print("two sum:", res)

