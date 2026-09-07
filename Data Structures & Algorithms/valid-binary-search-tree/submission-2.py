# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node,max_val,min_val):
            if not node:
                return True
            
            if node.val <= min_val or node.val >= max_val:
                return False
            
            left_result = dfs(node.left, node.val, min_val)
            right_result  = dfs(node.right, max_val, node.val)

            return left_result and right_result
            
        return dfs(root, float("inf"), float('-inf'))