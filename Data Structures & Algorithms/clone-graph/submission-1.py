"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        copies = {}
        def clone(node):
            if node is None:
                return None
            if node in copies:
                return copies[node]
            
            clone_node = Node(node.val)
            copies[node] = clone_node

            for neigbour in node.neighbors:
                cloned_neigbour = clone(neigbour)
                clone_node.neighbors.append(cloned_neigbour)
            
            return clone_node
        
        return clone(node)
        
        