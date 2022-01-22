class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_num = sys.maxsize
        
        for p in prices:
            min_num = min(min_num, p)
            max_profit = max(p-min_num, max_profit)
            
        return max_profit