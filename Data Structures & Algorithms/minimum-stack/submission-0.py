class MinStack:

    def __init__(self):
        self.items = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))

    def pop(self) -> None:
        self.items.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

