# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        
        def get_vals(node):
            if node:
                get_vals(node.left)
                nodes.append(node)
                get_vals(node.right)
        
        get_vals(root)
        
        vals = sorted(n.val for n in nodes)
        for i in range(len(vals)):
            nodes[i].val = vals[i]