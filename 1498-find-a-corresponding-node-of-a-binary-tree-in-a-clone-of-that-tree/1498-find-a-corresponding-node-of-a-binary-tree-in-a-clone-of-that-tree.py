# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(root1: TreeNode, root2: TreeNode) -> TreeNode:
            if root1 is None:
                return None
            if root1 == target:
                return root2
            return dfs(root1.left, root2.left) or dfs(root1.right, root2.right)

        return dfs(original, cloned)

        # node1, node2 = original, cloned
        # queue1, queue2 = deque(), deque()
        # if node1:
        #     queue1.append(node1)
        #     queue2.append(node2)
        # while queue1:
        #     for i in range(len(queue1)):
        #         node1 = queue1.popleft()
        #         node2 = queue2.popleft()
        #         if target == node1:
        #             return node2
        #         if node1.left:
        #             queue1.append(node1.left)
        #             queue2.append(node2.left)
        #         if node1.right:
        #             queue1.append(node1.right)
        #             queue2.append(node2.right)

        # def dfs(original_node, cloned_node):
        #     if not original_node:
        #         return None

        #     if original_node == target:
        #         return cloned_node

        #     left_result = dfs(original_node.left, cloned_node.left)
        #     if left_result:
        #         return left_result

        #     right_result = dfs(original_node.right, cloned_node.right)
        #     if right_result:
        #         return right_result

        # return dfs(original, cloned)
        