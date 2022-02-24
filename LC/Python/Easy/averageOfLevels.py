# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = collections.deque()
        q.append(root)
        
        while q:
            level_size = len(q)
            curr_sum = 0
            
            for i in range(level_size):
                curr = q.popleft()
                if curr:
                    curr_sum += curr.val
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                        
            if curr_sum:
                ans.append(curr_sum/level_size)
            else:
                ans.append(curr_sum)
        return ans