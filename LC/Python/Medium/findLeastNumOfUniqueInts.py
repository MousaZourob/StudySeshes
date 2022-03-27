class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        heap = []
        heapify(heap)
       
        for val, f in freq.items():
            heappush(heap, (f, val))
        
        while heap and k:
            count, num = heappop(heap)
            if k >= count:
                k -= count
            else:
                return len(heap) + 1
            
        return len(heap)