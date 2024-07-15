class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1376.Time%20Needed%20to%20Inform%20All%20Employees
        def dfs(i: int) -> int:
            ans = 0
            for j in g[i]:
                ans = max(ans, dfs(j) + informTime[i])
            return ans

        g = defaultdict(list)
        for i, x in enumerate(manager):
            g[x].append(i)
        return dfs(headID)
        
        def dfs(node):
            ans = 0
            for c in tree[node]:
                ans = max(ans, dfs(c))
            ans += informTime[node]
            return ans

        tree, n = defaultdict(list), len(manager)
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)
                
        return dfs(headID)
