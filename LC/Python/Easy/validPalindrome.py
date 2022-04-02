class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(a, b):
            while a <= b:
                if s[a] != s[b]:
                    return False
                a += 1
                b -= 1
            
            return True
        
        l, r  = 0, len(s) - 1
        
        while l <= r:
            if s[l] != s[r]:
                return is_pal(l, r-1) or is_pal(l+1, r)
            else:
                r -= 1
                l += 1
        
        return True