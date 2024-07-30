class Solution:
    # 长度为 3 的环，由三个顶点、三条边组成。我们假设三个顶点分别为 a, b, c。
    # 那么一定存在 c <=> a，c <=> b 以及 a <=> b，即环中的每个点都与其他两点直接相连。我们可以用哈希表来存放每个点的相邻点。
    # 由于环的长度为 3，每个相同的环会被重复统计 3 次，因此答案需除以 3。
    # 时间复杂度 
    # 空间复杂度 
    # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2077.Paths%20in%20Maze%20That%20Lead%20to%20Same%20Room
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        g = defaultdict(set)
        for a, b in corridors:
            g[a].add(b)
            g[b].add(a)
        ans = 0
        for i in range(1, n + 1):
            for j, k in combinations(g[i], 2):
                if j in g[k]:
                    ans += 1
        return ans // 3