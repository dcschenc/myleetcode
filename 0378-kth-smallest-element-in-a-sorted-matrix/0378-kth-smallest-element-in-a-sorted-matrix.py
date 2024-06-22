from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            heappush(min_heap, (matrix[i][0], i, 0))
        for _ in range(k-1):
            val, i, j = heappop(min_heap)
            if j < n-1:
                heappush(min_heap, (matrix[i][j+1], i, j + 1))
        return heappop(min_heap)[0]