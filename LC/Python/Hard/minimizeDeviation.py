from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums):
        def even(n):
            return 2 * n if n % 2 == 1 else n
        
        nums = SortedList([even(num) for num in nums])
        minn = nums[-1] - nums[0]
        
        while nums[-1] % 2 == 0:
            nums.add(nums[-1] // 2)
            nums.pop(-1)
            minn = min(minn, nums[-1] - nums[0])
        return minn