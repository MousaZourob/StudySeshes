class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1xn2 = 0
        
        for num in nums:
            n1xn2 ^= num
        
        right = 1
        while (right & n1xn2) == 0:
            right = right << 1
        
        num1, num2 = 0, 0
        
        for num in nums:
            if (num & right) != 0:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]