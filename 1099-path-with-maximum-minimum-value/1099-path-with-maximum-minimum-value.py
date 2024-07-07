import heapq
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # BFS + PriorityQueue O(n⋅m⋅log(n⋅m))
        m, n = len(grid), len(grid[0])
        heap = []        
        heapq.heappush(heap, (-grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))
        min_score = grid[0][0]
        while heap:
            score, r, c = heapq.heappop(heap)
            min_score = -score
            if r == m-1 and c == n-1:
                return min_score
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for i, j in neighbors:
                if 0<= i <= m-1 and 0<= j <=n-1 and (i, j) not in visited:
                    new_score = min(min_score, grid[i][j])
                    heapq.heappush(heap, (-new_score, i, j))
                    visited.add((i, j))
        return -1
                    

