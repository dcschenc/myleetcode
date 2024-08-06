class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:  
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2497.Maximum%20Star%20Sum%20of%20a%20Graph
        g = defaultdict(list)
        for a, b in edges:
            if vals[b] > 0:
                g[a].append(vals[b])
            if vals[a] > 0:
                g[b].append(vals[a])
        for bs in g.values():
            bs.sort(reverse=True)
        return max(v + sum(g[i][:k]) for i, v in enumerate(vals))
              
        # hm = defaultdict(list)
        # for u, v in edges:
        #     if vals[v] > 0:
        #         hm[u].append(vals[v])
        #     if vals[u] > 0:
        #         hm[v].append(vals[u])

        # mx = -float('inf')
        # # for k, v in hm.items():
        # n = len(vals)
        # for key in range(n):
        #     if key in hm:
        #         v = hm[key]
        #         v.sort(reverse=True) 
        #         mx = max(mx, vals[key] + sum(v[:k]))
        #     else:
        #         mx = max(mx, vals[key])
        # return mx