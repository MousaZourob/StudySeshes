# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        heap = []
        heapify(heap)
        
        def get_vals(node):
            if node:
                get_vals(node.left)
                if node.val not in heap:
                    heappush(heap, node.val)
                get_vals(node.right)
            
        get_vals(root)
        
        heappop(heap)
                
        return heap[0] if heap else -1