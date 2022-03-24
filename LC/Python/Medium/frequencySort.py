class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        
        for c in s:
            freq[c] += 1
        
        heap = []
        
        for char, freq in freq.items():
            heappush(heap, (-freq, char))
        
        ans = ""
        
        while heap:
            freq, char = heappop(heap)
            
            for _ in range(-freq):
                ans += char
        
        return ans