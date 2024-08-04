class Solution:
    # 排序 + 并查集
    # 要保证路径起点（终点）大于等于路径上的所有点，因此我们可以考虑先把所有点按值从小到大排序，然后再进行遍历，添加到连通块中，具体如下：
    # 当遍历到点 a 时， 对于小于等于 a 的邻接点 b
    #  来说，若二者不在同一个连通块，则可以合并，并且可以以点 
    #  所在的连通块中所有值为 a
    #  的点为起点，以点 b
    #  所在的连通块中所有值为 
    #  的点为终点，两种点的个数的乘积即为加入点 
    #  时对答案的贡献。
    # 时间复杂度 O(nlogn)
    # https://github.com/doocs/leetcode/blob/main/solution/2400-2499/2421.Number%20of%20Good%20Paths/README.md

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:           
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2421.Number%20of%20Good%20Paths
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        n = len(vals)
        p = list(range(n))
        size = defaultdict(Counter)
        for i, v in enumerate(vals):
            size[i][v] = 1

        ans = n
        for v, a in sorted(zip(vals, range(n))):
            for b in g[a]:
                if vals[b] > v:
                    continue
                pa, pb = find(a), find(b)
                if pa != pb:
                    ans += size[pa][v] * size[pb][v]
                    p[pa] = pb
                    size[pb][v] += size[pa][v]
        return ans