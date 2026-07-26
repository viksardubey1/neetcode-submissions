class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(char for char in s if char.isalnum()).lower()
        for i in range(len(cleaned_s)//2):
            if cleaned_s[i] != cleaned_s[-(i+1)]:
                return False
        return True
        