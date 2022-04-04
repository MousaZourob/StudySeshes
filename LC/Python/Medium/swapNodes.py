# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:     
        #find kth starting node
        k_start = k_end = head
        for _ in range(k-1):
            k_start = k_start.next
        
        #find kth ending node
        tail = k_start
        while tail.next:
            k_end = k_end.next
            tail = tail.next
        
        #swap
        k_start.val, k_end.val = k_end.val, k_start.val
        
        return head