def subset(arr):
    ans = []
    def backtrack(i, current_subset: list):
        # print(arr)
        # print("part:",current_subset)
    
        if len(arr) == i:
            print(current_subset)
            ans.append(list(current_subset))
            return
        current_subset.append(arr[i])
        backtrack(i+1, current_subset)
        current_subset.pop()
        backtrack(i+1, current_subset)


    backtrack(0, [])
    return ans



arr = [1,2]
res = subset(arr)
print(res)