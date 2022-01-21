class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        maximum = curr_sum
        for i in range(1, len(nums)-k+1):
            curr_sum -= nums[i-1]
            curr_sum += nums[i+k-1]
            maximum = max(maximum, curr_sum)
        return maximum / k