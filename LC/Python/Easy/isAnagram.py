class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table, t_table = {}, {}
        
        if len(s) != len(t): return False
        
        for i in range(len(s)):
            s_table[s[i]] = 1 + s_table.get(s[i], 0)
            t_table[t[i]] = 1 + t_table.get(t[i], 0)

        return s_table == t_table