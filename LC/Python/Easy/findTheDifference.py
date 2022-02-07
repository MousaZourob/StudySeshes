class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = Counter(s)
        tc = Counter(t)
        
        for c in tc:
            if not sc[c] == tc[c]:
                return c