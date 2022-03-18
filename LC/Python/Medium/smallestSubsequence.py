class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        last_occurance = {}
        
        for i, c in enumerate(s):
            last_occurance[c] = i
            
        for i, c in enumerate(s):
            if c not in stack:
                while stack and i < last_occurance[stack[-1]] and c < stack[-1]:
                    stack.pop()
                stack.append(c)
        
        return ''.join(stack)