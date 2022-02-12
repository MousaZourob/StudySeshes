class Solution:
    def intervalOverlap(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])

        for i in range(len(intervals)):
            if intervals[i][1] < intervals[i-1][0]:
                return True
        return False