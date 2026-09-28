class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, l = set(), 0
        max_length = 0
        for r in range(len(s)):
            while s[r] in longest:
                longest.remove(s[l])
                l += 1
            longest.add(s[r])
            max_length = max(max_length, len(longest))
        return max_length

