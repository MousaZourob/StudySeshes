class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()    
        ans = [[]]
        start, end = 0, 0
        
        for i in range(len(nums)):
            start = 0
            
            if i > 0 and nums[i] == nums[i - 1]:
                start = end + 1
                
            end = len(ans) - 1
            for j in range(start, end + 1):
                subset = list(ans[j])
                subset.append(nums[i])
                ans.append(subset)
        return ans