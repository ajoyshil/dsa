# Valid parenthses

def solution(n):
    def solve(s, n, open, close, res):
        # if open == n - 1 and close == n - 1:
        #     return res
        if len(s) == 2 * n:
            res.append(s)
            return
        if open < n:
            solve(s + "(", n, open + 1, close, res)
        if close < open:
            solve(s + ")", n, open, close + 1, res)
        return res

    return solve("", n, 0, 0, [])


print(solution(2))
