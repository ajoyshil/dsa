"""
This function will return index value if target found else it will return -1
"""
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (r + l) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


arr = [-1, 0, 3, 5, 6, 8, 22, 55]
print(binary_search(arr, 55))
