class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0847.Shortest%20Path%20Visiting%20All%20Nodes
        n = len(graph)
        q = deque()
        vis = set()
        for i in range(n):
            q.append((i, 1 << i))
            vis.add((i, 1 << i))
        ans = 0
        while 1:
            for _ in range(len(q)):
                i, st = q.popleft()
                if st == (1 << n) - 1:
                    return ans
                for j in graph[i]:
                    nst = st | 1 << j
                    if (j, nst) not in vis:
                        vis.add((j, nst))
                        q.append((j, nst))
            ans += 1



        n = len(graph)
        # target = (1 << n) - 1  # Target state with all nodes visited

        # (current_node, visited_nodes, cost)
        queue = deque([(i, {i}, 0) for i in range(n)])  
        visited = set()

        while queue:
            node, visited_nodes, cost = queue.popleft()

            if (node, tuple(visited_nodes)) in visited:
                continue

            visited.add((node, tuple(visited_nodes)))

            if len(visited_nodes) == n:
                return cost

            for neighbor in graph[node]:
                new_visited = visited_nodes | {neighbor}
                queue.append((neighbor, new_visited, cost + 1))

        return -1  # If no valid path is found