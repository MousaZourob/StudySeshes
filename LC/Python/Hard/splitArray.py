class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def split(largest):
            subarray_count = 1
            curr_sum = 0
            
            for n in nums:
                curr_sum += n
                
                if curr_sum > largest:
                    subarray_count += 1
                    curr_sum = n
                    
            return subarray_count <= m
            
        l, r = max(nums), sum(nums)
        ans = r
        
        while l <= r:
            mid = l + ((r - l) // 2)
            if split(mid):
                ans = mid
                r = mid  - 1
            else: 
                l = mid + 1
                
        return ans