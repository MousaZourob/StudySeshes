class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a, b = 0, 0
        ans = []
        
        while a < len(firstList) and b < len(secondList):
            start = max(firstList[a][0], secondList[b][0])
            end = min(firstList[a][1], secondList[b][1])
            
            if start <= end:
                ans.append([start, end])
            
            if firstList[a][1] < secondList[b][1]:
                a += 1
            else:
                b += 1
        
        return ans