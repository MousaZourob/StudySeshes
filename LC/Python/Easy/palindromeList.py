# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        
        while f and f.next:
            f = f.next.next
            s = s.next
        
        prev = None
        while s:
            temp = s.next
            s.next = prev
            prev = s
            s = temp
        
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
            