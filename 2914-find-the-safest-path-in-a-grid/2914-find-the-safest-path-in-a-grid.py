class UnionFind:
    """A class that implements the Union-Find (Disjoint Set) data structure."""
    # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2812.Find%20the%20Safest%20Path%20in%20a%20Grid
  
    def __init__(self, size):
        # Parent pointers initialised to point to themselves and sizes initialised to 1
        self.parent = list(range(size))
        self.set_size = [1] * size

    def find(self, x):
        """Finds the representative (root) of the set containing 'x'. Implements path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        """Unites the sets containing 'a' and 'b'. Return False if they are already in the same set, True otherwise."""
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
          
        # Union by size, making the smaller root point to the larger one
        if self.set_size[root_a] > self.set_size[root_b]:
            self.parent[root_b] = root_a
            self.set_size[root_a] += self.set_size[root_b]
        else:
            self.parent[root_a] = root_b
            self.set_size[root_b] += self.set_size[root_a]
        return True


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """Calculates the maximum safeness factor in a grid avoiding unsafe cells."""
        # Initialize variables
        n = len(grid)
        # If start or end cells are unsafe, return 0
        if grid[0][0] or grid[n - 1][n - 1]:
            return 0
          
        # BFS to find distances from unsafe cells
        queue = deque()
        dist = [[float('inf')] * n for _ in range(n)]
        # Seed initial distances for unsafe cells
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i, j))
                    dist[i][j] = 0
        # Directions for moving to adjacent cells
        directions = (-1, 0, 1, 0, -1)
        while queue:
            ci, cj = queue.popleft()
            for da, db in pairwise(directions):
                ni, nj = ci + da, cj + db
                if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] == float('inf'):
                    dist[ni][nj] = dist[ci][cj] + 1
                    queue.append((ni, nj))

        # Sort cells based on their distance from unsafe cells in descending order
        candidates = sorted(((dist[i][j], i, j) for i in range(n) for j in range(n)), reverse=True)
        uf = UnionFind(n * n)
        for d, i, j in candidates:
            # Attempt to connect current cell with all its neighbors
            for da, db in pairwise(directions):
                x, y = i + da, j + db
                if 0 <= x < n and 0 <= y < n and dist[x][y] >= d:
                    uf.union(i * n + j, x * n + y)
            # Check if start and end cells are connected
            if uf.find(0) == uf.find(n * n - 1):
                return int(d)
        return 0