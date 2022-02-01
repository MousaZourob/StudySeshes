class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        window_start = 0
        max_length = 0
        max_repeat_character = 0
        
        for window_end in range(len(s)):
            seen[s[window_end]] = seen.get(s[window_end], 0) + 1

            max_repeat_character = max(max_repeat_character, seen[s[window_end]])
            
            if window_end - window_start + 1 - max_repeat_character > k:
                seen[s[window_start]] -= 1
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length