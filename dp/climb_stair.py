class Solution:
    def climbStairs(self, n: int) -> int:
        d = [0] * (n + 1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        d[0] = 0
        d[1] = 1
        d[2] = 2

        for i in range(3, n + 1):
            d[i] = d[i - 1] + d[i - 2]
        print(d)
        return d[n]


a = 4

obj = Solution()
obj.climbStairs(a)