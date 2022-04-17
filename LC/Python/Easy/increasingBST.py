# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                nonlocal dummy
                
                inorder(node.left)
                dummy.right = TreeNode(node.val)
                dummy = dummy.right
                inorder(node.right)
        
        if not root:
            return None
        
        ans = TreeNode()
        dummy = ans
                
        inorder(root)
        
        return ans.right