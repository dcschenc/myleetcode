# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(node):
            if node:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)

        vals = []
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def build_bst(vals, lower=float('-inf'), upper=float('inf')):
            if not vals: return None
            val = vals[0]
            if not lower < val < upper:
                return None
            vals.pop(0)
            node = TreeNode(int(val))
            node.left = build_bst(vals, lower, val)
            node.right = build_bst(vals, val, upper)
            return node

        vals = [int(val) for val in data.split(",") if val]
        return build_bst(vals)

    # def serialize(self, root: Optional[TreeNode]) -> str:
    #     """Encodes a tree to a single string.
    #     """
    #     if not root:
    #         return 'null'
    #     left = self.serialize(root.left)
    #     right = self.serialize(root.right)
    #     return f'{root.val},{left},{right}'

    # def deserialize(self, data: str) -> Optional[TreeNode]:
    #     """Decodes your encoded data to tree.
    #     """
    #     def helper(values):
    #         val = values.pop(0)
    #         if val == 'null':
    #             return None
    #         node = TreeNode(int(val))
    #         node.left = helper(values)
    #         node.right = helper(values)
    #         return node


    #     values = data.split(',')
    #     return helper(values)

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans