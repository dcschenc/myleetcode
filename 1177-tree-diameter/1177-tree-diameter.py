from collections import deque, defaultdict
# https://leetcode.com/problems/tree-diameter/editorial/
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        def bfs(start):
          queue = deque()
          queue.append(start)
          visited = []
          dist = 0
          while queue:
              for i in range(len(queue)):
                  node = queue.popleft()               
                  visited.append(node)
                  for ch in adj[node]:
                      if ch not in visited:
                        queue.append(ch) 
              dist += 1
          return visited[-1], dist

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        last_node, _ = bfs(0)
        last_node, distance = bfs(last_node)
        return distance - 1