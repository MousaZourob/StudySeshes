class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = max(nums)
        curr_min, curr_max = 1,1
        
        for num in nums:
            if num == 0:
                curr_min, curr_max = 1,1
            else:
                tmp = num*curr_max
                curr_max = max(tmp, curr_min*num, num)
                curr_min = min(tmp, curr_min*num, num)
                max_prod = max(max_prod, curr_max)
        
        return max_prod