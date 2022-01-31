class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        seen = {}
        window_start = 0
        max_length = 0

        for window_end in range(len(s)):
            seen[s[window_end]] = seen.get(s[window_end], 0) + 1

            while len(seen) > k:
                seen[s[window_start]] -= 1
                if seen[s[window_start]] == 0:
                    del seen[s[window_start]]
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length