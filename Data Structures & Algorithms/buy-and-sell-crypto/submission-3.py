class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val, l = 0, 0
        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
            max_val = max(max_val, prices[r] - prices[l])
        return max_val


        