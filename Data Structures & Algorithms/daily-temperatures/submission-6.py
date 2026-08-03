class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for temp in temperatures]
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_ind = stack.pop()
                output[stack_ind] = i - stack_ind
            stack.append([t, i])
        return output


            

        