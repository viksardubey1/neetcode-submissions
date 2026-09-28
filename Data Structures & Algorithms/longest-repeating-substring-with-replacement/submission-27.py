class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_char, max_length = 0, 0, 0
        counts = {}
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_char = max(max_char, counts[s[r]])
            if (r - l + 1) - max_char > k:
                counts[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length


        