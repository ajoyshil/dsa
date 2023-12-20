def next_permutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1
    if i >= 0:
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
print(next_permutation(nums))
