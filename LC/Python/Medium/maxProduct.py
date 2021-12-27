def maxProduct(self, nums: List[int]) -> int:
    ans = max(nums)
    currMin, currMax = 1, 1
    
    for num in nums:
        if num == 0:
            currMin, currMax = 1, 1
        
        currMin, currMax = min(num * currMin, num * currMax, num), max(num * currMin, num * currMax, num)
        ans = max(ans, currMax) 
        
    return ans