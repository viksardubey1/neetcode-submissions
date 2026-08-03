class Solution:
    def isValid(self, s: str) -> bool:
        brack_dict = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []
        for c in s:
            if c in brack_dict:
                if not stack:
                    return False
                if brack_dict[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True
        