from collections import deque, defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1129.Shortest%20Path%20with%20Alternating%20Colors
        g = [defaultdict(list), defaultdict(list)]
        for i, j in redEdges:
            g[0][i].append(j)
        for i, j in blueEdges:
            g[1][i].append(j)

        ans = [-1] * n
        vis = set()
        q = deque([(0, 0), (0, 1)])
        d = 0
        while q:
            for _ in range(len(q)):
                i, c = q.popleft()
                if ans[i] == -1:
                    ans[i] = d
                vis.add((i, c))
                c ^= 1
                for j in g[c][i]:
                    if (j, c) not in vis:
                        q.append((j, c))
            d += 1
        return ans

        
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)
        red_distance = [-1] * n
        blue_distance = [-1] * n
        red_distance[0] = 0
        blue_distance[0] = 0
        queue = deque([(0, 'red', 0), (0, 'blue', 0)])
        while queue:
            cur, color, dist = queue.popleft()
            if color == 'red':
                for nb in blue_adj[cur]:
                    if blue_distance[nb] == -1:
                        blue_distance[nb] = dist + 1
                        queue.append((nb, 'blue', dist + 1))
            if color == 'blue':
                for nb in red_adj[cur]:
                    if red_distance[nb] == -1:
                        red_distance[nb] = dist + 1
                        queue.append((nb, 'red', dist + 1))
        result = []
        for i in range(n):
            min_dist = min(red_distance[i], blue_distance[i])
            if min_dist == -1:
                min_dist = max(red_distance[i], blue_distance[i])
            result.append(min_dist)
        return result