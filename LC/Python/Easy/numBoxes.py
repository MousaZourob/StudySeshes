class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        
        boxTypes = sorted(boxTypes, key = lambda l:l[1], reverse = True)
        
        for l in boxTypes:
            box_amount = min(truckSize, l[0])
            ans += min(truckSize, l[0]) * l[1]
            truckSize -= box_amount
        
        return ans