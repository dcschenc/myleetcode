class Solution:
    ####  BFS ######
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == n

        visit = [False]*len(rooms)
        q = deque()
        q.append(0)
        while q:
            cur = q.popleft()
            visit[cur] = True
            for v in rooms[cur]:
                if not visit[v]:
                    q.append(v)
        return all(visit)


    #####  DFS ######
    # def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    #     visited = [0]*len(rooms)
    #     def dfs(i):
    #         visited[i] = 1
    #         for j in rooms[i]:
    #             if visited[j] != 1:
    #                 dfs(j)
    #                 # visited[j] = 1
    #     dfs(0)
    #     # print(visited)
    #     if 0 not in visited:
    #         return True
    #     return False