from itertools import combinations
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2316.Count%20Unreachable%20Pairs%20of%20Nodes%20in%20an%20Undirected%20Graph
        def dfs(node):
            if visited[node]:
                return 0            
            visited[node] = True
            ans = 1
            for c in graph[node]:                
                ans += dfs(c)
            return ans
        
        # groups = []
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans, s = 0, 0
        for node in range(n):
            if visited[node] is False:
                cur = dfs(node)
                ans += cur * s
                s += cur
                # groups.append(dfs(node))
        # ans = 0
        # print(len(groups))
        # m = len(groups)
        
        # for m, n in combinations(groups, 2):
            # ans += m * n
        return ans