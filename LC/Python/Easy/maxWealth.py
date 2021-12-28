class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        test = [sum(a) for a in accounts]
        return max(test)