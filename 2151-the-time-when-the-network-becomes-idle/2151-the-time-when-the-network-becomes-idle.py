class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2039.The%20Time%20When%20the%20Network%20Becomes%20Idle
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        q = deque([0])
        vis = {0}
        ans = d = 0
        while q:
            d += 1
            t = d * 2
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if v not in vis:
                        vis.add(v)
                        q.append(v)
                        ans = max(ans, (t - 1) // patience[v] * patience[v] + t + 1)
        return ans
        
        # First we calculate the shortest latency ( amount of time it takes for a message to reach the master server plus the time it takes for a reply to reach back the server ) for every node.
        # Then from their patience time, we calculate for each node, the last time it sends a message before it recieves a reply.
        # Finally our answer is the maximum of the time for each node from the time they send the first message to the time they recieve a reply for their last message

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            
        dis = {}
        queue = deque([(0, 0)])
        visited = set([0])
        while queue:
            cur, length = queue.popleft()
            dis[cur] = length * 2
            for nxt in graph[cur]:
                if nxt not in visited:
                    queue.append((nxt, length + 1))
                    visited.add(nxt)
        
        ans = -float("inf")
        for i in range(1, len(patience)):
            if patience[i] < dis[i]:
                rem = dis[i] % patience[i]
                lastCall = dis[i] - (rem) if rem > 0 else dis[i] - patience[i]
                ans = max(ans, lastCall + dis[i]) 
            else:
                ans = max(ans, dis[i])
        return ans + 1