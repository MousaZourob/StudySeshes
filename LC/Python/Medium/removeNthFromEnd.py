# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        curr = head
        listSize = 0
        while curr:
            listSize += 1
            curr = curr.next
        
        if n == listSize:
            return head.next
        
        curr = head
        for i in range(listSize-1-n):
            curr = curr.next 
        curr.next = curr.next.next
        
        return head
    