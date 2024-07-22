# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1660.Correct%20a%20Binary%20Tree
        def dfs(node):
            if node is None or node.right in visited:
                return None
            visited.add(node)
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            return node

        visited = set()
        return dfs(root)

        queue = deque()
        queue.append((root, None, False))
        while queue:
            cur = []
            nodes = set()
            for _ in range(len(queue)):
                node, parent, left = queue.popleft()
                if node.left:
                    queue.append((node.left, node, True))
                if node.right:
                    queue.append((node.right, node, False))
                cur.append((node, parent, left))
                nodes.add(node)
            
            for node, parent, left in cur:
                if node.right and node.right in nodes:
                    if left:
                        parent.left = None
                    else:
                        parent.right = None
                    node.right = None
                    return root
        


        