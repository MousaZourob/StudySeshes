class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Write your code here
        seen = set()
        window_start = 0
        max_length = 0

        for window_end in range(len(s)):
            while s[window_end] in seen:
                seen.remove(s[window_start])
                window_start += 1
            
            seen.add(s[window_end])
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length