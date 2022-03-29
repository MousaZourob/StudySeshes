class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapify(heap)
        
        for r in matrix:
            for n in r:
                heappush(heap, -n)
                if len(heap) > k:
                    heappop(heap)

        return -heap[0]