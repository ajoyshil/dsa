# Python program for the above approach

# Function to find the possible
# permutations
def permutations(res, nums, l, h):
    # Base case
    # Add the vector to result and return
    if (l == h):
        res.append(nums.copy())

        return

    # Permutations made
    for i in range(l, h + 1):
        # Swapping
        nums[l], nums[i] = nums[i], nums[l]
        # next greater value of l
        permutations(res, nums, l + 1, h)

        # Backtracking
        nums[l], nums[i] = nums[i], nums[l]


# Function to get the permutations
def permute(nums):
    # Declaring result variable
    x = len(nums) - 1
    res = []

    # Calling permutations for the first
    # time by passing l
    # as 0 and h = nums.size()-1
    permutations(res, nums, 0, x)
    return res


# Driver Code
nums = [1, 2, 3]
res = permute(nums)
print(res)
for i in res:
    print(i)

# This code is contributed by Saurabh Jaiswal
