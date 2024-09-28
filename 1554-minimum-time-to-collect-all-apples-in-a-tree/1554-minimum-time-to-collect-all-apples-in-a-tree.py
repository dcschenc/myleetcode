class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(current_node, cost_to_come_back):
            if visited[current_node]:
                return 0
            visited[current_node] = True
          
            # Accumulated cost of visiting children nodes.
            total_cost = 0
            for child_node in graph[current_node]:
                total_cost += dfs(child_node, 2)
          
            # If there's no apple at the current node, and no cost accumulated from children,
            # it means we don't need to collect any apples on this path.
            if not hasApple[current_node] and total_cost == 0:
                return 0          
            return cost_to_come_back + total_cost

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
      
        visited = [False] * n
      
        return dfs(0, 0)
