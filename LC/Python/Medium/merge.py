class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        ans = [intervals[0]]

        for interval in intervals[1:]:
            last_end = ans[-1][1]

            if interval[0] <= last_end:
                ans[-1][1] = max(last_end, interval[1])
            else:
                ans.append(interval)

        return ans