class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == '+':
                stack.append(stack.pop() + stack.pop())
            elif val == '-':
                stack.append((stack.pop() - stack.pop()) * -1)
            elif val == '*':
                stack.append(stack.pop() * stack.pop())
            elif val == '/':
                stack.append(int(1 / stack.pop() * stack.pop()))
            else:
                stack.append(int(val))
        return stack[-1]

        