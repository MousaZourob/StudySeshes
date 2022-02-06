class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3: return 
        
        non_dupe_count = 2
        
        for i in range(2, len(nums)):
            if nums[non_dupe_count - 2] != nums[i]:
                nums[non_dupe_count] = nums[i]
                non_dupe_count += 1
        
        return non_dupe_count