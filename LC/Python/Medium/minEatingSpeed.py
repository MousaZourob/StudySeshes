class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        
        while l <= r:
            mid = (l+r)//2
            
            total_time = 0
            for pile in piles:
                total_time += ceil(pile/mid)
            
            if total_time <= h:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        
        return ans