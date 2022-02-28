# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = collections.deque()
        q.append(root)
        
        while q:
            ans += 1
            curr_level = []
            level_size = len(q)
            
            for i in range(level_size):
                curr = q.popleft()
                if curr:
                    curr_level.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
        
        return ans