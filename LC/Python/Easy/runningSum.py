class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currSum = 0
        ans = []
        
        for num in nums:
            ans.append(num + currSum)
            currSum += num
        
        return ans