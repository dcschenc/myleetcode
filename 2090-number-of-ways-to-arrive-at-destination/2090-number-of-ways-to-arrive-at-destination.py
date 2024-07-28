from collections import defaultdict
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1976.Number%20of%20Ways%20to%20Arrive%20at%20Destination
        mod = 10**9 + 7
        adj = defaultdict(list)
        for r1, r2, cost in roads:
            adj[r1].append((r2, cost))
            adj[r2].append((r1, cost))

        min_time = [float('inf')] * n
        ways_to_reach = [0] * n
        min_time[0] = 0
        ways_to_reach[0] = 1

        # (time, intersection)
        pq = [(0, 0)]  
        while pq:
            cur_time, cur_node = heapq.heappop(pq)
            if cur_time > min_time[cur_node]:
                continue                
            for nb, time in adj[cur_node]:
                if cur_time + time < min_time[nb]:
                    min_time[nb] = cur_time + time
                    ways_to_reach[nb] = ways_to_reach[cur_node]
                    heapq.heappush(pq, (min_time[nb], nb))
                elif cur_time + time == min_time[nb]:
                    ways_to_reach[nb] = (ways_to_reach[nb] + ways_to_reach[cur_node]) % mod

        return ways_to_reach[n - 1] % mod

        # def dfs(cur, path, time):
        #     nonlocal hm
        #     if cur == n-1:
        #         hm[time] += 1
        #         return
        #     path.add(cur)
        #     for nb, cost in adj[cur]:
        #         if nb not in path:
        #             dfs(nb, path, time + cost)
        #     path.remove(cur)
        
        # hm = defaultdict(int)
        # adj = defaultdict(list)
        # for r1, r2, cost in roads:
        #     adj[r1].append((r2, cost))
        #     adj[r2].append((r1, cost))
        # dfs(0, set(), 0)
        
        # sorted_items = sorted(hm.items())
        # return sorted_items[0][1] % (10**9 + 7)
