# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # node = root
        # while k < node.val:
        #     node = node.left
        stack = []
        curr = root
        visited = set()
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if k - curr.val in visited:
                    return True
                else:
                    visited.add(curr.val)
                curr = curr.right
        return False