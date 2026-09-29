class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bph_hi, bph_lo = max(piles), 1
        final_min = float("inf")
        while bph_hi >= bph_lo:
            bph_mid = (bph_hi + bph_lo) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / bph_mid)
            if hours <= h:
                final_min = min(final_min, bph_mid)
                bph_hi = bph_mid - 1
            else:
                bph_lo = bph_mid + 1
        return final_min

            


        
        