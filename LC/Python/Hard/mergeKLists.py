# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapify(heap)
        
        for i, l in enumerate(lists):
            if l: 
                heappush(heap,(l.val, i))
        
        ans = ListNode(0)
        dummy = ans
        
        while heap:
            val, i = heappop(heap)
            
            dummy.next = ListNode(val)
            dummy = dummy.next
            
            if lists[i].next:
                heappush(heap, (lists[i].next.val, i))
                lists[i] = lists[i].next
        
        return ans.next