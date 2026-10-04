class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda l, r: l + r,
            '-': lambda l, r: l - r,
            '*': lambda l, r: l * r,
            '/': lambda l, r: int(l / r),
        }
        stack = []
        for t in tokens:
            if t in ops:
                r, l = stack.pop(), stack.pop()  
                stack.append(ops[t](l, r))
            else:
                stack.append(int(t))    
        return stack[0]
