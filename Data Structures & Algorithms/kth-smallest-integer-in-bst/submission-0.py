# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count

            if not node:
                return

            left_res = dfs(node.left)
            if left_res:
                return left_res

            count += 1
            if count == k:
                return node.val
            
            right_res = dfs(node.right)
            if right_res:
                return right_res
                
        return dfs(root)
