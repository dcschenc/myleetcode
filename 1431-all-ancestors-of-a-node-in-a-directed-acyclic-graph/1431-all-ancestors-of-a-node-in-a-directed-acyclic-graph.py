from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2192.All%20Ancestors%20of%20a%20Node%20in%20a%20Directed%20Acyclic%20Graph
        def bfs(s: int):
            q = deque([s])
            vis = {s}
            while q:
                i = q.popleft()
                for j in g[i]:
                    if j not in vis:
                        vis.add(j)
                        q.append(j)
                        ans[j].append(s)

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
        ans = [[] for _ in range(n)]
        for i in range(n):
            bfs(i)
        return ans


        adj = defaultdict(list)
        degree = [0] * n
        ans = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            degree[v] += 1
        # print(degree, adj)
        queue = deque()
        for i in range(n):
            if degree[i] == 0:
                queue.append((i, set()))
        while queue:
            for i in range(len(queue)):
                node, path = queue.popleft()
                ans[node] = sorted(list(path))
                path.add(node)
                for child in adj[node]:
                    degree[child] -= 1
                    if degree[child] == 0:
                        queue.append((child, path | set(ans[child])))
                    else:
                      ans[child].extend(list(path))        
        return ans