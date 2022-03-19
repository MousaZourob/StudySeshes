class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1n2 = 0
        ans = [0, 0]
        
        for num in nums:
            n1n2 ^= num
        
        n1n2 &= -n1n2
        
        for num in nums:
            if n1n2 & num:
                ans[0] ^= num
            else:
                ans[1] ^= num
        
        return ans