class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        heapify(max_heap)
        min_heap = []
        heapify(min_heap)
        
        for i, c in enumerate(capital):
            heapq.heappush(min_heap, (c, i))
        
        for _ in range(k):
            while min_heap and min_heap[0][0] <= w:
                cap, index = heappop(min_heap)
                heappush(max_heap, (-profits[index], index))
            
            if not max_heap:
                break
            
            w += -heappop(max_heap)[0]
        
        return w