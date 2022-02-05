class MinStack:

    def __init__(self):
        self.stack =[]
        return 

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack)==0:
            return
        else:
            return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        else:
            return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return
        else:
            return min(self.stack)
