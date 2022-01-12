# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr_node = ListNode()
        ans = curr_node
        
        while l1 or l2:
            temp = 0
            if l1:
                temp = l1.val
            if l2:
                temp += l2.val
            
            temp += carry
            curr_sum = temp % 10
            carry = temp // 10

            curr_node.next = ListNode(curr_sum)
            curr_node = curr_node.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
         
        if carry > 0:
            curr_node.next = ListNode(carry)
        
        return ans.next