class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        non_dupe_count = 1

        for i in range(len(nums)):
            if nums[non_dupe_count - 1] != nums[i]:
                nums[non_dupe_count] = nums[i]
                non_dupe_count += 1
        
        for i in range(non_dupe_count, len(nums)):
            nums.pop(non_dupe_count)