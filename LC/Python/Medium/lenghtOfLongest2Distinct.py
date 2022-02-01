class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Write your code here
        seen = {}
        window_start = 0
        max_length = 0

        for window_end in range(len(s)):
            seen[s[window_end]] = seen.get(s[window_end], 0) + 1

            while len(seen) > 2:
                seen[s[window_start]] -= 1
                if seen[s[window_start]] == 0:
                    del seen[s[window_start]]
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length