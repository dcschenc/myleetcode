# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2096.Step-By-Step%20Directions%20From%20a%20Binary%20Tree%20Node%20to%20Another
        def dfs(node, parent, direction):
            if parent:
                graph[node].append((parent, 'U'))
                graph[parent].append((node, direction))
            if node.left:
                dfs(node.left, node, 'L')
            if node.right:
                dfs(node.right, node, 'R')

        graph = defaultdict(list)
        dfs(root, None, '')
        queue = deque()
        visited = set()
        for node in graph:
            if node.val == startValue:
                queue.append((node, ''))
                break
        while queue:
            for _ in range(len(queue)):
                node, path = queue.popleft()
                if node.val == destValue:
                    return path
                if node in visited:
                    continue
                visited.add(node)
                for nb, direction in graph[node]:
                    queue.append((nb, path + direction))
            
