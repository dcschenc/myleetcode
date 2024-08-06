class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2492.Minimum%20Score%20of%20a%20Path%20Between%20Two%20Cities
        def dfs(i):
            nonlocal ans
            for j, d in g[i]:
                ans = min(ans, d)
                if not vis[j]:
                    vis[j] = True
                    dfs(j)

        g = defaultdict(list)
        for a, b, d in roads:
            g[a].append((b, d))
            g[b].append((a, d))
        vis = [False] * (n + 1)
        ans = inf
        dfs(1)
        return ans

        # def dfs(node):
        #     if node in nodes:
        #         return            
        #     nodes.add(node)
        #     for c in graph[node]:
        #         dfs(c)

        # graph = defaultdict(list)
        # # weights = {}
        # for u, v, w in roads:
        #     graph[u].append(v)
        #     graph[v].append(u)
        #     # weights[(u, v)] = w
        #     # weights[(v, u)] = w
        # nodes = set()
        # ans = float('inf')
        # dfs(1)
        # # for u, v in combinations(nodes, 2):
        # #     if (u, v) in weights:
        # #         ans = min(ans, weights[(u, v)])
        # for u, v, w in roads:
        #     if u in nodes and v in nodes:
        #         ans = min(ans, w)
        # return ans
