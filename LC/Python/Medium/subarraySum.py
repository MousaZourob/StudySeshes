class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        ans = 0
        curr_sum = 0
        
        for n in nums:
            curr_sum += n
            
            ans += prefix[curr_sum - k]
            prefix[curr_sum] += 1
        
        return ans