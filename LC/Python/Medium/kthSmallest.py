class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapify(heap)

        for l in matrix:
            heappush(heap, (l[0], 0, l))
        
        num = 0
        
        while heap:
            num, index, lst = heappop(heap)
            
            k -= 1
            if k == 0: 
                break
                
            if len(lst) > index + 1:
                heappush(heap, (lst[index+1], index+1, lst))
        
        return num