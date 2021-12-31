class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        n = Counter(nums)
        
        for key in n:
            if k == 0:
                if n[key] > 1:
                    ans += 1
            else:
                if key + k in n:
                    ans += 1
                    
        return ans