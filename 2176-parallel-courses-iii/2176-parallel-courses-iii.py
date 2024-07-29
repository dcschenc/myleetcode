class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2050.Parallel%20Courses%20III        g = defaultdict(list)
        graph = defaultdict(list)
        indeg = [0] * n
        for a, b in relations:
            graph[a - 1].append(b - 1)
            indeg[b - 1] += 1
        queue = deque()
        dp = [0] * n
        ans = 0
        for i, (v, t) in enumerate(zip(indeg, time)):
            if v == 0:
                queue.append(i)
                dp[i] = t
                ans = max(ans, t)
        while queue:
            i = queue.popleft()
            for j in graph[i]:
                dp[j] = max(dp[j], dp[i] + time[j])
                ans = max(ans, dp[j])
                indeg[j] -= 1
                if indeg[j] == 0:
                    queue.append(j)
        return ans