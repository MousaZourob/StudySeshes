# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(curr, curr_path, ans):
            if not curr: return False
            
            curr_path.append(str(curr.val))
            if not curr.right and not curr.left:
                ans.append("->".join(curr_path))
            else:
                dfs(curr.right, curr_path, ans)
                dfs(curr.left, curr_path, ans)
            
            curr_path.pop()
        
        dfs(root, [], ans)
        
        return ans
            