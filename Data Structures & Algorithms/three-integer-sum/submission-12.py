class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = set()
        for i in range(len(sorted_nums)):
            target = 0 - sorted_nums[i]
            left, right = i + 1, len(sorted_nums) - 1
            while left < right:
                if sorted_nums[left] + sorted_nums[right] > target:
                    right -= 1
                elif sorted_nums[left] + sorted_nums[right] < target:
                    left += 1
                else:
                    res.add((sorted_nums[i], sorted_nums[left], sorted_nums[right]))
                    right -= 1
                    left += 1
        return [list(item) for item in res]



