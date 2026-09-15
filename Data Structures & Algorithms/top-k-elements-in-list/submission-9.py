class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {num: 0 for num in set(nums)}
        for num in nums:
            freq_dict[num] += 1
        sorted_freq_dict = sorted(freq_dict.items(), key = lambda item: item[1], reverse = True)
        return [value[0] for value in sorted_freq_dict[:k]]
        