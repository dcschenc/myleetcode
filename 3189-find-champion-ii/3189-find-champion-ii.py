class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2924.Find%20Champion%20II
        degree = [0] * n
        for u, v in edges:
            degree[v] += 1
        
        res = [i for i in range(n) if degree[i] == 0]
        
        return res[0] if len(res) == 1 else -1