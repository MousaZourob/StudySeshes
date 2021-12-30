class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None: return root
        
        lNode = root
        while lNode.left != None:
            head = lNode
            while head != None:
                head.left.next = head.right
                if head.next != None:
                    head.right.next = head.next.left
                head = head.next
            
            lNode = lNode.left
        
        return root