class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        exp = len(columnTitle) - 1
        
        for c in columnTitle:
            temp = ord(c) - ord('A') + 1
            ans += 26 ** exp * temp
            exp -= 1
        
        return ans