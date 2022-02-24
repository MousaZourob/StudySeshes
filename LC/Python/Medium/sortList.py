# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMid(self, head):
        s, f = head, head.next
        
        while f and f.next:
            f = f.next.next
            s = s.next
        return s
    
    def merge(self, left, right):
        ans = ListNode()
        runner = ans
        
        while left and right:
            if left.val > right.val:
                runner.next = right
                right = right.next
            else:
                runner.next = left
                left = left.next
            runner = runner.next

            
        if left:
            runner.next = left
        if right:
            runner.next = right
        
        return ans.next