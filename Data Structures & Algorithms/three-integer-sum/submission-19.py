class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            target = 0 - sorted_nums[i]
            while l < r:
                if sorted_nums[l] + sorted_nums[r] > target:
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < target:
                    l += 1
                elif sorted_nums[l] + sorted_nums[r] == target:
                    res.add((sorted_nums[i], sorted_nums[l], sorted_nums[r]))
                    l += 1
                    r -= 1
        return [result for result in res]
            


        