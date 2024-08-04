# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if not node:
                return 
            if node.left:
                dfs(node.left)
                tree[node.val].append(node.left.val)
                tree[node.left.val].append(node.val)
            if node.right:
                dfs(node.right)
                tree[node.val].append(node.right.val)
                tree[node.right.val].append(node.val)
            
        tree = defaultdict(list)
        dfs(root)
        minutes, visited = 0, set()
        queue = deque([start])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                for c in tree[cur]:
                    if c not in visited:
                        queue.append(c)
            minutes += 1
        return minutes - 1
