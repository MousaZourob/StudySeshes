class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for c in t:
            if len(s) == ptr:
                break
            if s[ptr] == c:
                ptr += 1
        
        return len(s) == ptr