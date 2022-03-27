class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        heapify(heap)
        ans = []
        
        for i in range(len(mat)):
            heappush(heap, (mat[i].count(1), i))
            
        for _ in range(k):
            ans.append(heappop(heap)[1])
                
        return ans