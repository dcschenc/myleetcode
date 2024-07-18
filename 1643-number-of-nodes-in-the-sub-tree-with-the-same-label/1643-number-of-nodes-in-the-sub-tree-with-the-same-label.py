class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1519.Number%20of%20Nodes%20in%20the%20Sub-Tree%20With%20the%20Same%20Label
        def dfs(i, fa):
            ans[i] -= cnt[labels[i]]
            cnt[labels[i]] += 1
            for j in g[i]:
                if j != fa:
                    dfs(j, i)
            ans[i] += cnt[labels[i]]

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        cnt = Counter()
        ans = [0] * n
        dfs(0, -1)
        return ans
        
        def dfs(node):            
            counter = defaultdict(int)
            for c in tree[node]:
                subtree = dfs(c)
                for k, v in subtree.items():
                    counter[k] += v
                # counter.update(dfs(c))
            c = labels[node]
            counter[c] += 1
            ans[node] = counter[c]
            # print(node, counter)
            return counter

        ans = [0] * n
        tree = defaultdict(list)
        nodes = set()
        for u, v in edges:
            if u == 0 or u in nodes:
                tree[u].append(v)
                nodes.add(v)
            else:
                tree[v].append(u)
                nodes.add(u)


        dfs(0)
        return ans