class MinStack:

    def __init__(self):
        self.queue = []
        
    def push(self, val: int) -> None:
        if(len(self.queue) == 0):
            self.queue.append((val,val))
        else:
            self.queue.append((val,min(val,self.queue[-1][1])))

    def pop(self) -> None:
        self.queue.pop(-1)

    def top(self) -> int:
        return self.queue[-1][0]

    def getMin(self) -> int:
        return self.queue[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()