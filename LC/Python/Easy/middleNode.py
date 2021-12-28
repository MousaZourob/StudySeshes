# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        countNode = head
        
        while countNode != None:
            count += 1
            countNode = countNode.next
            
        ans = head
        for i in range(count//2):
            ans = ans.next
            
        return ans