from collections import defaultdict
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        @cache
        def dfs(i):
            # if ans[i] is not None:
                # return ans[i]
            ans[i] = i
            for j in adj[i]:
                candidate = dfs(j)
                if quiet[candidate] < quiet[ans[i]]:
                    ans[i] = candidate
            return ans[i]
        
        adj = defaultdict(list)
        for u, v in richer:
            adj[v].append(u)        
        n = len(quiet)
        ans = [None] * n
        for i in range(n):            
            dfs(i)
            
        return ans

        # def dfs(node):
        #     # if node in res:
        #         # return
        #     res.append(node)
        #     for v in adj[node]:
        #         if v not in res:
        #             dfs(v)
        
        # adj = defaultdict(list)
        # for u, v in richer:
        #     adj[v].append(u)        
        # n = len(quiet)
        # ans = [i for i in range(n)]
        # for i in range(n):
        #     res = []
        #     dfs(i)
        #     idx = -1
        #     quietest = float('inf')
        #     for j in res:
        #         if quiet[j] < quietest:
        #             idx = j
        #             quietest = quiet[j]
        #     ans[i] = idx
        # return ans