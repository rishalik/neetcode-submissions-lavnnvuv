class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recursion

        # def dfs(i):
        #     n = len(nums)
        #     if i >= n:
        #         return 0
        #     return max(dfs(i+1), nums[i]+dfs(i+2))
        # return dfs(0)
        
        # DP - top down

        # n = len(nums)
        # memo = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if memo[i] != -1:
        #         return memo[i]
        #     memo[i] = max(dfs(i+1), nums[i]+dfs(i+2))
        #     return memo[i]
        # return dfs(0)
    
        # DP - bottom up

        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        memo = [0] * n
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        for i in range(2, n):
            memo[i] = max(memo[i-1], nums[i]+memo[i-2])
        return memo[-1]




