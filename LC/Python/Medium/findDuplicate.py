class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 0
        ans = []
        
        while start < len(nums):
            j = nums[start] - 1
            if j < len(nums) and nums[start] != nums[j]:
                nums[start], nums[j] = nums[j], nums[start]
            else:
                start += 1
        
        return nums[-1]