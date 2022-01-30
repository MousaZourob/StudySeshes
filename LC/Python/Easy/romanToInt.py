class Solution:
    def romanToInt(self, s: str) -> int:
        s_to_v = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i == len(s)-1 or s_to_v[s[i]] >= s_to_v[s[i+1]]:
                ans += s_to_v[s[i]]
            else:
                ans -= s_to_v[s[i]]
                
        return ans