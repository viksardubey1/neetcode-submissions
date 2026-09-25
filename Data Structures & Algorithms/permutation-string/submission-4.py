class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        l = 0
        for r in range(len(sorted_s1) - 1, len(s2)):
            if sorted(s2[l:r+1]) == sorted_s1:
                return True
            l += 1
        return False



        