class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        # def count(x):
        #     return sum(bisect_right(row, x) for row in grid)

        # m, n = len(grid), len(grid[0])
        # target = (m * n + 1) >> 1
        # return bisect_left(range(10**6 + 1), target, key=count)

        m, n = len(grid), len(grid[0])        
        heap = []
        mid = m * n // 2 + 1
        cnt = 0
        for r in range(m):
            heappush(heap, (grid[r][cnt], r, 0))
        while cnt <= mid:
            val, r, c = heappop(heap)
            cnt += 1
            if c + 1 < n:
                heappush(heap, (grid[r][c+1], r, c + 1))
            if cnt == mid:
                return val


        # pos = [0] * m
        # mid = m * n // 2 + 1
        # prev = float('inf')
        # cnt = 0
        # print(mid, m, n)
        # while cnt < mid:
        #     prev = float('inf')
        #     for i in range(m):
        #         if pos[i] < n and grid[i][pos[i]] <= prev:
        #             prev = grid[i][pos[i]]
        #             pos[i] += 1
        #             cnt += 1
        # return prev

[[71575,109387,113328,258018,317748,327741,385646,423299,489324,563784,612475,725022,728067,750414,769846,824496,899884],
[19324,36317,61462,112157,286730,300583,313241,345757,483842,586927,733078,743581,752183,774762,871565,944784,956649],
[2165,63036,66552,186476,217978,235978,265673,315636,328790,417180,442602,557679,566878,598316,614081,813774,969910]]