# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        
        def dfs(curr, curr_path, ans):
            if not curr: return
            
            curr_path.append(str(curr.val))
            
            if not curr.right and not curr.left:
                ans.append(int(''.join(curr_path)))
            else:
                dfs(curr.right, curr_path, ans)
                dfs(curr.left, curr_path, ans)
        
            curr_path.pop()
        
        dfs(root, [], ans)
        
        return sum(ans)