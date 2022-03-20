class FreqStack:
    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        
        if self.freq[val] > len(self.stack):
            self.stack.append([val])
        else:
            self.stack[self.freq[val] - 1].append(val)
        
    def pop(self) -> int:
        val = self.stack[-1].pop()
        
        if not self.stack[-1]:
            self.stack.pop()
        self.freq[val] -= 1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()