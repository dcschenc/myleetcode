class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1631.Path%20With%20Minimum%20Effort
        row = len(heights)
        col = len(heights[0])
        diff = [[math.inf] * col for _ in range(row)]
        diff[0][0] = 0
        visited = [[False]*col for _ in range(row)]
        queue = [(0, 0, 0)]  # difference, x, y
        while queue:
            difference, x, y = heapq.heappop(queue)
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                    cur = abs(heights[nx][ny]-heights[x][y])
                    max_difference = max(cur, diff[x][y])
                    if diff[nx][ny] > max_difference:
                        diff[nx][ny] = max_difference
                        heapq.heappush(queue, (max_difference, nx, ny))
        return diff[-1][-1]

        row = len(heights)
        col = len(heights[0])
        self.max_so_far = math.inf

        def dfs(x, y, max_difference):
            if x == row-1 and y == col-1:
                self.max_so_far = min(self.max_so_far, max_difference)
                return max_difference
            current_height = heights[x][y]
            heights[x][y] = 0
            min_effort = math.inf
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < row and 0 <= ny < col and heights[
                        nx][ny] != 0:
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y]-current_height)
                    max_current_difference = max(
                        max_difference, current_difference)
                    if max_current_difference < self.max_so_far:
                        result = dfs(adjacent_x, adjacent_y,
                                     max_current_difference)
                        min_effort = min(min_effort, result)
            heights[x][y] = current_height
            return min_effort

        return dfs(0, 0, 0)