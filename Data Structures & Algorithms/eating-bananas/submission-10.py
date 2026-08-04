from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        lo, hi = 1, max_k
        while lo <= hi:
            mid = (hi + lo) // 2
            if self.check_eats(mid, piles) > h:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
    
    def check_eats(self, k, piles):
        hours = 0
        for pile in piles:
            hours += ceil(pile / k)
        return hours


        


        