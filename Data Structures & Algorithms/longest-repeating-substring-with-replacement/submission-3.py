class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, max_char, l = 0, 0, 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_char = max(max_char, count[s[r]])
            while len(s[l:r + 1]) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, len(s[l:r + 1]))
        return res

