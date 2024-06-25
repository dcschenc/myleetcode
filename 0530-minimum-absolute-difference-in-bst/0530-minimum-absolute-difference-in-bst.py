# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            nonlocal prev, min_diff
            # if not node:
            #     return 
            if node.left:
                inorder(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            # res.append(node.val)
            if node.right:
                inorder(node.right)
        
        # res = []
        prev = None
        min_diff = float('inf')
        inorder(root)
        return min_diff
        # print(res)
        # diff = abs(res[1] - res[0])
        # for i in range(1,len(res)):
        #     new_diff = abs(res[i] - res[i-1])
        #     if  new_diff < diff:
        #         diff = new_diff
        # return diff
