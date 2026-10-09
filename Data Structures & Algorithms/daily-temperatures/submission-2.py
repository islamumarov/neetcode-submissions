class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n-1, -1, -1):
            while max_stack and temperatures[max_stack[-1]] <= temperatures[i]:
                max_stack.pop()
            
            if max_stack and temperatures[max_stack[-1]] >= temperatures[i]:
                res[i] = max_stack[-1] - i

            max_stack.append(i)

        return res



