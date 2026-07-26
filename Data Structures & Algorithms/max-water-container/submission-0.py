class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        r = len(heights) - 1
        l = 0
        while r > l:
            max_area = max(min(heights[r], heights[l]) * (r - l), max_area)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return max_area



        