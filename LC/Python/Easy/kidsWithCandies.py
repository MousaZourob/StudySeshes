class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_candies = max(candies)
        
        for candy in candies:
            ans.append(candy + extraCandies >= max_candies)
        
        return ans