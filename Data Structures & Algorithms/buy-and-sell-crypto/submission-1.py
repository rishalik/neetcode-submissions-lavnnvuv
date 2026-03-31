class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_s = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_s = max(profit, max_s)
            else:
                l = r
            r += 1
        return max_s