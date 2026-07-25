class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {key: 0 for key in set(nums)}
        for num in nums:
            nums_dict[num]+=1
        sorted_list = sorted(nums_dict.items(), key = lambda item: item[1], reverse=True)
        return [value[0] for value in sorted_list[:k]]


            

        