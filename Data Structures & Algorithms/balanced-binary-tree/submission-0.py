# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0
            
            l_h = dfs(node.left)
            if l_h == -1:
                return -1

            r_h = dfs(node.right)
            if r_h == -1:
                return -1
            
            if abs(r_h - l_h) > 1:
                return -1
            
            return max(r_h, l_h) + 1
        
        return dfs(root) != -1