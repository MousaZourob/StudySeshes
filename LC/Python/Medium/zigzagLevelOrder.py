# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        zig = True
        
        ans = []
        q = collections.deque()
        q.append(root)
        
        while q:
            levelSize = len(q)
            curr_level = []
            
            for i in range(levelSize):
                curr = q.popleft()
                if curr:
                    if zig:
                        curr_level.append(curr.val)
                    else:
                        curr_level.insert(0, curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                        
            if curr_level:
                ans.append(curr_level)
            
            zig = not zig
        
        
        return ans