class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def operatate(nums, func):
            a, b = nums.pop(), nums.pop()
            res = func(b,a)
            nums.append(int(res))

        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] not in {'+', '-', '*', '/'}:
                stack.append(int(tokens[i]))
            elif tokens[i] == '+':
                operatate(stack, lambda a,b: a + b)
            elif tokens[i] == '-':
                operatate(stack, lambda a,b: a - b)
            elif tokens[i] == '*':
                operatate(stack, lambda a,b: a * b)
            elif tokens[i] == '/':
                operatate(stack, lambda a,b: a / b)
        
        return stack[0]

