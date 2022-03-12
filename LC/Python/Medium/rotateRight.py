# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        
        tail = head 
        list_length = 1
        
        while tail.next:
            tail = tail.next
            list_length += 1
        
        k = k % list_length
        
        if k == 0: return head
        
        pivot = head
        for _ in range(list_length - k - 1):
            pivot = pivot.next 

        start = pivot.next
        pivot.next = None
        tail.next = head
        
        return start