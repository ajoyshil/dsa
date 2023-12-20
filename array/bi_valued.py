def solution(A):
    # Implement your solution here
    ans = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            s = set(A[i:j+1])
            if len(s)>2:
                continue
            ans = max(ans, len(A[i:j+1]))
            # print(A[i:j+1])
    return ans

print(solution([0, 5, 4, 4, 5, 12]))

A = ["abc", "de", "efg"]

def longest_string(A):
    max_len = 0
    for i in range(len(A)):
        hash_set = set()
        for j in range(i, len(A)):
            for char in A[j]:
                if char in hash_set:
                    break
            else:
                hash_set.update(A[j])
                curr = ''.join(A[k] for k in range(i, j + 1))
                max_len = max(max_len, len(curr))
    return max_len

print(longest_string(A))