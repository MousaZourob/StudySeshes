# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createTree(nums, start, end):
            if start > end:
                return None

            mid = (start  + end) // 2
            n = TreeNode(nums[mid])
            n.left = createTree(nums, start, mid-1)
            n.right = createTree(nums, mid+1, end)
            return n
        
        return createTree(nums, 0, len(nums)-1)