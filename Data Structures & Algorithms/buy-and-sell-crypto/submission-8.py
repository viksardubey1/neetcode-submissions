class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        for r in range(1, len(prices)):
            while prices[l] > prices[r]:
                l += 1
            max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit

        