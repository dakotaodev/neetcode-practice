class MyQueue:

    def __init__(self):
        self.s1: list[int]=[] # contains the elements in the order they are received
        self.s2: list[int]=[] # contains the elements of s1 flushed in reverse order

    def push(self, x: int) -> None:
        self.s1.append(x) 

    def pop(self) -> int: 
        if not self.s2: # meaning that we dont have the reverse order, we must flush s1
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s2), len(self.s1)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()