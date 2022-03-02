# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        ans[0] = float('-inf')
        
        def dfs(curr):
            if not curr: return 0
            
            right = dfs(curr.right)
            left = dfs(curr.left)
            
            if not right or right < 0:
                right = 0
            if not left or left < 0:
                left = 0
            
            curr_sum = curr.val + right + left
            ans[0] = max(ans[0], curr_sum)
            
            return max(right, left) + curr.val
            
        dfs(root)
        
        return ans[0]