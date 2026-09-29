class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_order = []
        self.size = 0

    def push(self, val: int) -> None: 
        self.stack.append(val)
        val = min(val, self.stack_order[-1] if self.stack_order else val)
        self.stack_order.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_order.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_order[-1]


        
