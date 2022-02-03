class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        keep_elem = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[keep_elem] = nums[i]
                keep_elem += 1
        
        for i in range(keep_elem, len(nums)):
            nums.pop(keep_elem)