class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        start = 0
        ans = []
        
        while start < len(nums):
            j = nums[start] - 1
            if j < len(nums) and nums[start] != nums[j]:
                nums[start], nums[j] = nums[j], nums[start]
            else:
                start += 1
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(nums[i])
        
        return ans