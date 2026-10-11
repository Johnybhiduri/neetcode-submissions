# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def dfs(node):
            if node:
                current_val = node.val
                if node.left:
                    left_val = dfs(node.left)
                    if left_val:
                        output.append(left_val)

                output.append(node.val)

                if node.right:
                    right_val = dfs(node.right)
                    if right_val:
                        output.append(right_val)


        dfs(root)
        return output