class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        endAt = defaultdict(list)
        for s, e, t in rides:
            endAt[e].append((s, e - s + t))
        
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            for s, t in endAt[i]:
                dp[i] = max(dp[i], t + dp[s])
         
        return dp[-1]