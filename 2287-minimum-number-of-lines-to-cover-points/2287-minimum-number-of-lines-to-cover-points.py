class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2152.Minimum%20Number%20of%20Lines%20to%20Cover%20Points
        def check(i, j, k):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)

        @cache
        def dfs(state):
            if state == (1 << n) - 1:
                return 0
            ans = inf
            for i in range(n):
                if not (state >> i & 1):
                    for j in range(i + 1, n):
                        nxt = state | 1 << i | 1 << j
                        for k in range(j + 1, n):
                            if not (nxt >> k & 1) and check(i, j, k):
                                nxt |= 1 << k
                        ans = min(ans, dfs(nxt) + 1)
                    if i == n - 1:
                        ans = min(ans, dfs(state | 1 << i) + 1)
            return ans

        n = len(points)
        return dfs(0)

        def cal_lamda(p1, p2):
            if p1[0] == p2[0]:
                return float('inf')           
            return (p1[1] - p2[1]) / (p1[0] - p2[0])


        def backtrack(points, cnt):
            if len(points) == 0:
                ans[0] = min(ans[0], cnt)
                return
            if len(points) <= 2:
                ans[0] = min(ans[0], cnt + 1)
                return
            n = len(points)
            for i in range(n):
                for j in range(i + 1, n):
                    if i != j:
                        next_points = [points[k] for k in range(n) if k != i and k != j and
                        slopes[tuple(points[k] + points[j])] != slopes[tuple(points[j] + points[i])]]
                        backtrack(next_points, cnt + 1)

        slopes = {}
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i != j:
                    slopes[tuple(points[i] + points[j])] = cal_lamda(points[i], points[j])
        # visited = [False] * n
        ans = [len(points)]        
        backtrack(points, 0)
        return ans[0]