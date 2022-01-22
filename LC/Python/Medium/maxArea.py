class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0
        min_h = 0
        
        while l < r:
            min_h = min(height[l], height[r])
            area = (r-l)*min_h
            max_area = max(area, max_area)
            
            while height[l] <= min_h and l < r:
                l = l+1
            while height[r] <= min_h and l < r:
                r = r-1
            
        return max_area