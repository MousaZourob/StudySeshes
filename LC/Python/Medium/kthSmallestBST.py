# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        heap = []
        heapify(heap)
        
        def get_vals(node):
            if node:
                get_vals(node.left)
                heappush(heap, node.val)
                get_vals(node.right)
            
        get_vals(root)
        
        for _ in range(k - 1):
            heappop(heap)
                
        return heap[0]