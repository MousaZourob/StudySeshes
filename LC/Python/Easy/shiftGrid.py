class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nums = []
        ans = []
        row_len = len(grid[0])
        
        for row in grid:
            nums.extend(row)
        
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        
        start = 0
        for _ in range(len(grid)):
            ans.append(nums[start:row_len + start])
            start += row_len
        
        return ans