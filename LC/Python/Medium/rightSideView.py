# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = collections.deque()
        q.append(root)
        
        while q:
            level_size = len(q)
            curr_level = []
            
            for _ in range(level_size):
                curr = q.popleft()
                
                if curr:
                    curr_level.append(curr.val)
                
                    if curr.right:
                        q.append(curr.right)
                    if curr.left:
                        q.append(curr.left)
            
            if curr_level:
                ans.append(curr_level[0])

        return ans