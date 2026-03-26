# Find a^b using recursion
# Base Case
# solution(n) = n* solution(n-1)

def solution(a, b):
    if b == 1:
        return a
    return a * solution(a, b-1)


print(solution(3, 4))


