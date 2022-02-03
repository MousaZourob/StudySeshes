class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            
            while l < r:
                curr_sum = sum((nums[i], nums[l], nums[r]))
                if abs(curr_sum-target) < abs(ans-target):
                    ans = curr_sum
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    return ans
        return ans