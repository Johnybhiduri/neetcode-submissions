# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(current):
            if current.val > p.val and current.val > q.val:
                if current.left:
                    return dfs(current.left)
            
            if current.val < p.val and current.val < q.val:
                if current.right:
                    return dfs(current.right)
            
            return current
        
        return dfs(root)
                