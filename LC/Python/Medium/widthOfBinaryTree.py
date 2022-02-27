# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = [(0, root)]
        
        while q:
            curr_level = []
            level_size = len(q)
            
            for i in range(level_size):
                index, curr = q.pop(0)
                curr_level.append(index)
                if curr.left:
                    q.append((index*2 + 1, curr.left))
                if curr.right:
                    q.append((index*2 + 2, curr.right))
            
            ans = max(ans, max(curr_level)-min(curr_level)+1)
            
        return ans