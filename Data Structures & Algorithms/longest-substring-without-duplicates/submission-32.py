class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        working_set = set()
        max_length, l = 0, 0
        for r in range(len(s)):
            while s[r] in working_set:
                working_set.remove(s[l])
                l += 1
            working_set.add(s[r])
            max_length = max(max_length, len(working_set))
        return max_length

        