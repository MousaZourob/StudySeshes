class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        ans = []
        
        curr_range = [nums[0]]
        for num in nums[1:]:
            if num - 1 != curr_range[-1]:
                if len(curr_range) > 1:
                    ans.append(f'{curr_range[0]}->{curr_range[-1]}')
                else:
                    ans.append(str(curr_range[0]))
                curr_range = []
            curr_range.append(num)
        
        if len(curr_range) > 1:
            ans.append(f'{curr_range[0]}->{curr_range[-1]}')
        else:
            ans.append(str(curr_range[0]))
        
        return ans