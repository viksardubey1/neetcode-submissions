class Solution:
    def findMin(self, nums: List[int]) -> int:
        # for [3,4,5,6,1,2], lo = 0, hi = 5, mid = 2
        lo, hi = 0, len(nums) - 1
        while hi > lo:
            mid = (hi + lo) // 2 
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[hi]

            

        