class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = [0]*n
        
        for i in range(n-1, -1, -1):
            val = min(26, k - i)
            ans[i] = chr(97+val-1)
            k -= val
            
        return ''.join(ans)