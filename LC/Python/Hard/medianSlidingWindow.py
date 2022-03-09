from sortedcontainers import SortedList
class Solution:
    def balanceTree(self, h1, h2):
        while len(h1) > len(h2) + 1:
                heapq.heappush(h2, -heapq.heappop(h1))
        while len(h2) > len(h1) + 1:
            heapq.heappush(h1, -heapq.heappop(h2))

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        
        max_heap = []
        heapq.heapify(max_heap)
        min_heap = []
        heapq.heapify(min_heap)
        
        for i, num in enumerate(nums):
            if not max_heap or -max_heap[0] < num:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappush(max_heap, -num)

            self.balanceTree(max_heap, min_heap)
            
            if i + 1 >= k:
                if len(max_heap) > len(min_heap):
                    ans.append(-max_heap[0])
                elif len(max_heap) < len(min_heap):
                    ans.append(min_heap[0])
                else:
                    ans.append((-max_heap[0] + min_heap[0]) / 2.0)
                
                removed = nums[i - k + 1]
                if max_heap and removed <= -max_heap[0]:
                    index = max_heap.index(-removed)
                    max_heap[index] = max_heap[-1]
                    max_heap.pop()
                    heapq.heapify(max_heap)
                else:
                    index = min_heap.index(removed)
                    min_heap[index] = min_heap[-1]
                    min_heap.pop()
                    heapq.heapify(min_heap)
            
            self.balanceTree(max_heap, min_heap)   
            
        return ans