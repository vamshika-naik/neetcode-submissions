class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(minimum)

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("pop from empty stack")

        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("empty stack")

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack:
            raise IndexError("empty stack")

        return self.minstack[-1]
