class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        
        a = 0
        b = 1
        
        for i in range(n):
            c = a + b
            a = b
            b = c
        
        return a