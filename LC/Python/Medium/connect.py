"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ans = []
        q = collections.deque()
        q.append(root)
        
        while q:
            level_size = len(q)
            curr_level = []
            
            for _ in range(level_size):
                curr = q.popleft()
                
                if curr:
                    curr_level.append(curr)
                    
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            
            for i in range(len(curr_level)-1):
                curr_level[i].next = curr_level[i+1]
        
        return root