class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) < 2:
            return [-1]

        ans = [0]*len(intervals)
        start_vals = []
        end_vals = []
        
        for i in range(len(intervals)):
            start_vals.append((intervals[i][0], i))
            end_vals.append((intervals[i][1], i))
        
        start_vals.sort()
        end_vals.sort()
        
        for i in range(len(end_vals)):
            l, r = 0, len(start_vals) - 1
            index = -1
            
            while l <= r:
                mid = (l + r) // 2
                
                if start_vals[mid][0] >= end_vals[i][0]:
                    index = start_vals[mid][1]
                    r = mid - 1
                else:
                    l = mid + 1
                    
            ans[end_vals[i][1]] = index
        
        return ans