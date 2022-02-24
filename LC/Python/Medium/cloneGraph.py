"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}
        
        def helper(node):
            if not node:
                return node
            elif id(node) in mapping:
                return mapping[id(node)]
            
            mapping[id(node)] = Node(node.val, [])
            
            for original_neighbor in node.neighbors:
                mapping[id(node)].neighbors.append(helper(original_neighbor))
            
            return mapping[id(node)]
        
        return helper(node)