# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.global_max = 0
        self.dfs(root)
        return self.global_max
    
    def dfs(self, curr):
        if not curr:
            return float('inf'), float('-inf')
        
        left_min, left_max = self.dfs(curr.left)
        right_min, right_max = self.dfs(curr.right)
        
        local_min = min(left_min, right_min, curr.val)
        local_max = max(left_max, right_max, curr.val)
        self.global_max = max(self.global_max, abs(curr.val - local_min), abs(curr.val-local_max))
        return local_min, local_max