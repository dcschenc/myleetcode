# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def getNode(root):  
            if root.val == target:
                return 0, root
            elif root.val > target:
                prev = root.val - target
                if root.left:
                    cur, node = getNode(root.left)
                    if cur <= prev:
                        return cur, node
                    else:
                        return prev, root
                return prev, root
            else:
                prev = target - root.val
                if root.right:
                    cur, node = getNode(root.right)
                    if cur < prev:
                        return cur, node
                    else:
                        return prev, root
                return prev, root
        val, node = getNode(root)
        return node.val