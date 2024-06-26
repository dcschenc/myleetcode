# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, d):
            if not node:
                return
            if d == depth - 1:
                # Insert new nodes at the specified depth
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
            else:
                # Continue the depth-first search
                dfs(node.left, d + 1)
                dfs(node.right, d + 1)
                
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        dfs(root, 1)
        return root

        if depth == 1:
            node = TreeNode(val, left=root)
            return node
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            level += 1
            if level == depth - 1:
                for i in range(len(queue)):
                    cur = queue.pop()
                    node = TreeNode(val)
                    node.left = cur.left
                    cur.left = node
                    node = TreeNode(val)
                    node.right = cur.right
                    cur.right = node
                break

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)        
        return root
