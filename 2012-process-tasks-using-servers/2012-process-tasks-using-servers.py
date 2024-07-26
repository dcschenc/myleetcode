class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1882.Process%20Tasks%20Using%20Servers
        availables = []
        for s, w in enumerate(servers):
            heappush(availables, (w, s))
        occupied = []
        ans = []
        for i, time in enumerate(tasks):
            while occupied and occupied[0][0] <= i:
                server = heappop(occupied)[2]
                heappush(availables, (servers[server], server))
            if availables:
                weight, server = heappop(availables)
                heappush(occupied, (i + time, weight, server))
            else:
                t, weight, server = heappop(occupied)           
                heappush(occupied, (t + time, weight, server))
            ans.append(server)
        return ans

