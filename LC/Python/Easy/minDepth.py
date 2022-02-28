# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = float('inf')
        q = collections.deque()
        q.append(root)
        
        curr_depth = 0
        while q:
            level_size = len(q)
            curr_level = []
            curr_depth += 1
            
            for _ in range(level_size):
                curr = q.popleft()
                if curr:
                    curr_level.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                if not curr.right and not curr.left:
                    ans = min(curr_depth, ans)
        
        return ans