class Solution:
    def brokenCalc(self, start: int, target: int) -> int:
        ans = 0
        
        while start < target:
            ans += 1
            if target % 2: target += 1
            else: target //= 2
            
        return ans + start - target