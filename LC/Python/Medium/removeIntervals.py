class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : (i[0], -i[1]))
        ans = [intervals[0]]
        
        for start, end in intervals[1:]:
            prev_start, prev_end = ans[-1]
            
            if prev_start <= start and prev_end >= end:
                continue
                
            ans.append([start, end])
                
        return len(ans)