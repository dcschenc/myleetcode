# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        queue = deque([root])
        visited = set()
        while queue:
            this_level = False
            for _ in range(len(queue)):
                node = queue.popleft()
                if this_level:
                    return node
                if node == u:
                    this_level = True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if this_level:
                return None
        # return None
        