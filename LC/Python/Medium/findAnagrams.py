class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        s_count, p_count = defaultdict(int), defaultdict(int)
        for i in range(len(p)):
            p_count[p[i]] += 1
            s_count[s[i]] += 1
        
        ans = [0] if s_count == p_count else []
        window_start = 0
        print(p_count)
        for window_end in range(len(p), len(s)):
            s_count[s[window_end]] += 1
            s_count[s[window_start]] -= 1
            
            if s_count[s[window_start]] == 0:
                s_count.pop(s[window_start])
            window_start += 1
            
            if s_count == p_count:
                ans.append(window_start)
            
            
        return ans