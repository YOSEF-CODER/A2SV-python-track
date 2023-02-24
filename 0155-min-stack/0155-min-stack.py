class MinStack:

    def __init__(self):
        self.stack=[]
        self.minn=[]

    def push(self, val: int) -> None:
        if self.minn:
            if val<=self.minn[-1]:
                self.minn.append(val) 
        else:
            self.minn.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack and self.minn:
            popped=self.stack.pop()
            if self.minn[-1]==popped:
                self.minn.pop() 
        elif self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minn:
            return self.minn[-1]
        return self.stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()