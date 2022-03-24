class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
        
        heap = []
        
        for num, freq in freq.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        
        ans = [row[1] for row in heap]
        
        return ans