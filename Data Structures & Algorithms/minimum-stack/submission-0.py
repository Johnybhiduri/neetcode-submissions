class MinStack:

    def __init__(self):
        self.stack  = []
        self.minStack = [] # save minimum at given index in stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            last_val = self.minStack[-1]
            min_val = min(last_val, val)
            self.minStack.append(min_val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]