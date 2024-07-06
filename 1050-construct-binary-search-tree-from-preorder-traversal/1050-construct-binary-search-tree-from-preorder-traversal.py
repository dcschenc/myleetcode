# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        # for i in range(1, len(preorder)):
            # if preorder[i] > preorder[0]:
                # break
        # if preorder[-1] < preorder[0]:
            # i = i + 1
        
        idx = bisect_right(preorder[1:], preorder[0]) + 1
        # print(idx)

        root.left = self.bstFromPreorder(preorder[1:idx])        
        root.right = self.bstFromPreorder(preorder[idx:])
        return root