class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0
        for item in nums_set:
            if item - 1 in nums_set:
                continue
            temp_length = 0
            temp = item
            while temp in nums_set:
                temp_length+=1
                temp+=1
            length = max(length, temp_length)
        return length
                
        
        