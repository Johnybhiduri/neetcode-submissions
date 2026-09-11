# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        in_ord_map = {num:idx for idx, num in enumerate(inorder)}
        idx = 0
        
        def dfs(left, right):
            nonlocal idx
            if left > right:
                return None

            root_val = preorder[idx] # Find the root val
            root = TreeNode(root_val) # create root node
            idx += 1 

            root_pos  = in_ord_map[root_val] # Find root position in inorder

            root.left = dfs(left, root_pos - 1) # create left  of root
            root.right = dfs(root_pos + 1, right) # create right of root

            return root

        return dfs(0,len(inorder)-1)