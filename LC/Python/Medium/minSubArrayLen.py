class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_sum, window_start, curr_sum = math.inf, 0, 0

        for window_end in range(len(nums)):
            curr_sum += nums[window_end]

            while curr_sum >= target:
                len_sum = min(len_sum, (window_end - window_start + 1))
                curr_sum -= nums[window_start]
                window_start += 1

        if len_sum == math.inf:
            return 0
        
        return len_sum