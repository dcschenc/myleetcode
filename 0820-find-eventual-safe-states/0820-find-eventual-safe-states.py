from collections import deque, defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:  
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0802.Find%20Eventual%20Safe%20States
        nbs = defaultdict(list)
        indeg = [0] * len(graph)
        for i, vs in enumerate(graph):
            for j in vs:
                nbs[j].append(i)
            indeg[i] = len(vs)
        q = deque([i for i, v in enumerate(indeg) if v == 0])

        while q:
            i = q.popleft()
            for j in nbs[i]:
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
