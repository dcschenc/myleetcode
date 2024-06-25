# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inOrderTraversal(node):
            nonlocal cur_val, cur_count, max_count, modes
            if not node:
                return
            # Recursively traverse the left subtree.
            inOrderTraversal(node.left)
            
            # Update mode and frequency information.
            if node.val == cur_val:
                cur_count += 1
            else:
                cur_val = node.val
                cur_count = 1

            if cur_count > max_count:
                max_count = cur_count
                modes = [cur_val]
            elif cur_count == max_count:
                modes.append(cur_val)

            # Recursively traverse the right subtree.
            inOrderTraversal(node.right)

        if not root:
            return []

        # Initialize variables to keep track of mode and frequency.
        modes = []
        cur_val = None
        cur_count = 0
        max_count = 0
        inOrderTraversal(root)
        return modes

        # def inorder(node):
        #     if not node:
        #         return
        #     if node.left:
        #         inorder(node.left)
        #     res.append(node.val)
        #     if node.right:
        #         inorder(node.right)
        
        # node = root
        # res = []
        # inorder(node)
        # # print(Counter(res).most_common(1))
        # ans = []
        # freq = Counter(res).most_common()
        # cnt = freq[0][1]
        # for i, j in freq:
        #     if j == cnt:
        #         ans.append(i)
        #     else:
        #         break
        # return ans
         
        # return [x[0] for x in Counter(res).most_common(1)]