class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif val == '-':
                stack.append(-1 * int(stack.pop()) + int(stack.pop()))
            elif val == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif val =='/':
                stack.append(1 / int(stack.pop()) * int(stack.pop()))
            else:
                stack.append(val)
        return int(stack[-1])