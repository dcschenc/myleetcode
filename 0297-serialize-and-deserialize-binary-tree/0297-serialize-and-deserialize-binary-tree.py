# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        """Encodes a tree to a single string."""

        if not root:
            return "null"

        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return f"{root.val},{left},{right}"

        # if not root:
        #     return ''
        # levels = [root]
        # res = str(root.val) + ','
        # while len(levels) > 0:
        #     curr_level = []
        #     for node in levels:
        #         if node.left:
        #             curr_level.append(node.left)
        #             res += str(node.left.val) + ','
        #         else:
        #             res += 'N,'
                    
        #         if node.right:
        #             curr_level.append(node.right)
        #             res += str(node.right.val) + ','
        #         else:
        #             res += 'N,'
        #     levels = curr_level
        # res = res.strip(',')
        # while res[-1] == 'N' or res[-1] == ',':
        #     res = res[:-1]
        # return res
                    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def helper(values):
            value = values.pop(0)
            if value == "null":
                return None
            node = TreeNode(int(value))
            node.left = helper(values)
            node.right = helper(values)                
            return node
        values = data.split(",")
        return helper(values)

        # if data == '':
        #     return None
        # data = data.split(',')
        # root = TreeNode(int(data[0]))
        # node = root
        # levels = [root]
        # idx = 1
        # while idx < len(data):
        #     curr_level = []
        #     for node in levels:
        #         if not node:
        #             continue
        #         if idx > len(data) -1 :
        #             break
        #         val = data[idx]
        #         idx += 1
        #         node.left = None
        #         if val != 'N':
        #             node.left = TreeNode(int(val))
        #         if idx > len(data) -1 :
        #             break
        #         val = data[idx]
        #         idx += 1
        #         if val != 'N':
        #             node.right = TreeNode(int(val))
        #         curr_level.append(node.left)
        #         curr_level.append(node.right)
        #     levels = curr_level
        # return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))