class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
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