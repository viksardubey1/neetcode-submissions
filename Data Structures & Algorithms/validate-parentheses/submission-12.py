class Solution:
    def isValid(self, s: str) -> bool:
        character_list = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack = []
        for char in s:
            if char in character_list:
                if not stack or stack.pop() != character_list[char]:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True
        