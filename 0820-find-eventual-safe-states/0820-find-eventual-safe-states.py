from collections import deque, defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:  
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0802.Find%20Eventual%20Safe%20States
        rg = defaultdict(list)
        indeg = [0] * len(graph)
        for i, vs in enumerate(graph):
            for j in vs:
                rg[j].append(i)
            indeg[i] = len(vs)
        q = deque([i for i, v in enumerate(indeg) if v == 0])
        while q:
            i = q.popleft()
            for j in rg[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return [i for i, v in enumerate(indeg) if v == 0]
              
        def dfs(i):
            if i in safe:
                return safe[i]
            ## cycle ##
            if i in visited:
                return False
            if not graph[i]:
                safe[i] = True
                return True
            visited.add(i)
            is_safe = True
            for nb in graph[i]:
                if not dfs(nb):
                    is_safe = False
            safe[i] = is_safe
            return safe[i]

        safe = {}
        for i in range(len(graph)):
            visited = set()
            dfs(i)

        return sorted([i for i in safe if safe[i]])

        # def dfs(node):
        #     if node in safe:
        #         return True
        #     if node in path:
        #         return False
        #     if len(graph[node]) == 0:
        #         safe.add(node)
        #         return True
        #     path.add(node)
        #     for nb in graph[node]:
        #         res = dfs(nb)
        #         if not res:
        #             return False
        #     # path.remove(node)  # Backtrack
        #     safe.add(node)
        #     return True

        # safe = set()
        # for i in range(len(graph)):
        #     path = set()
        #     if i not in safe:
        #         dfs_result = dfs(i)
        #         if dfs_result:
        #             safe.add(i)

        # return sorted(safe)