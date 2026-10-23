# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def dfs(node):
            nonlocal result
            if node is None:
                result.append("null")
                return
            
            result.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list  = data.split(",")
        index = 0
        def build():
            nonlocal index
            value = data_list[index]
            index += 1
            if value == "null":
                return 

            node = TreeNode(val=int(value))

            node.left = build()
            node.right = build()

            return node
        
        return build()

