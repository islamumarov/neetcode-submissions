class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'[': ']', '{' : '}', '(' : ')'}
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if not stack or  c != opening[stack.pop()]:
                    return False
        

        return not stack


