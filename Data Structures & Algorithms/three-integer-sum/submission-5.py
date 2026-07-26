class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        final_list = set()
        for i in range(len(nums)):
            target = 0 - sorted_nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] > target:
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < target:
                    l += 1
                else:
                    final_list.add((sorted_nums[i], sorted_nums[l], sorted_nums[r]))
                    l += 1
                    r -= 1
        return [list(item) for item in final_list]
                



        