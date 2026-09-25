class Solution:
    def isValid(self, s: str) -> bool:
        brack_dict = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }
        stack = []
        for char in s:
            if char in brack_dict:
                if not stack:
                    return False
                if brack_dict[char] != stack.pop():
                    return False
            else:
                stack.append(char)
                
        if stack:
            return False
        else:
            return True
        