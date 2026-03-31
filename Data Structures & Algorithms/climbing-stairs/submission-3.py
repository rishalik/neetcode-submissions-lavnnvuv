class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursion

        # def dps(i):
        #     if i >= n:
        #         return i == n
        #     return dps(i+1) + dps(i+2)
        # return dps(0)

        # DP - top down
        
        cache = [-1] * n
        def dps(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dps(i+1) + dps(i+2)
            return cache[i]
        return dps(0)

        # DP - botton up

        # if n <= 2:
        #     return n
        # dp = [0] * (n+1)
        # dp[1], dp[2] = 1, 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[i]


