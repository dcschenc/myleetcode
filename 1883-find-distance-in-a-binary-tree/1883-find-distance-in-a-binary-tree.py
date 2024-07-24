# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def lca(root, p, q):
            if root is None or root.val in [p, q]:
                return root
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
            if left is None:
                return right
            if right is None:
                return left
            return root

        def dfs(root, v):
            if root is None:
                return -1
            if root.val == v:
                return 0
            left, right = dfs(root.left, v), dfs(root.right, v)
            if left == right == -1:
                return -1
            return 1 + max(left, right)

        g = lca(root, p, q)
        return dfs(g, p) + dfs(g, q)
        
        def dfs(node, parent):            
            if parent:
                graph[parent].append(node)
                graph[node].append(parent)
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        if not root.left and not root.right:
            return 0
        graph = defaultdict(list)
        dfs(root, None)
        queue = deque()
        for node in graph:
            if node.val == p:
                queue.append(node)
                break
        visited = set()
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val == q:
                    return steps
                if node in visited:
                    continue
                visited.add(node)
                for nb in graph[node]:
                    queue.append(nb)
            steps += 1
        
