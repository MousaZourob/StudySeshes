class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compDic = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] in compDic:
                return [compDic[nums[i]], i]
            else:
                compDic[comp] = i