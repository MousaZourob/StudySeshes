class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        last_index = {}
        
        for i in range(len(s)):
            last_index[s[i]] = i
            
        end = 0
        size = 0
        for i in range(len(s)):
            end = max(end, last_index[s[i]])
            size += 1
            
            if i >= end:
                ans.append(size)
                size = 0
                
        return ans