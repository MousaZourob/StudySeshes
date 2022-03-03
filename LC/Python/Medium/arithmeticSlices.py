class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        window_start = 0
        ans = 0
        
        for window_end in range(len(nums)):
            if window_end - window_start < 2:
                continue
            
            if nums[window_end] - nums[window_end - 1] == nums[window_start + 1] - nums[window_start]:
                ans += window_end - window_start - 1
            else:
                window_start = window_end - 1
        
        return ans