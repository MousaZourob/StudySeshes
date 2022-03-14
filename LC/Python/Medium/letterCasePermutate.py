class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [s]
        for i in range(len(s)):
            if s[i].isalpha():
                for j in range(len(ans)):
                    chars = list(ans[j])
                    
                    if chars[i] == chars[i].lower():
                        chars[i] = chars[i].upper()
                    else:
                        chars[i] = chars[i].lower()
                    ans.append(''.join(chars))
                    
        return ans