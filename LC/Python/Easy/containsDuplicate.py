class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return Counter(nums) != Counter(set(nums))