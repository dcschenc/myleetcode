class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(i, j):
            for r in range(3):
                if sum(grid[i+r][j+k] for k in range(3)) != 15:
                    return False
            for c in range(3):
                if sum(grid[i+k][j+c] for k in range(3)) != 15:
                    return False            
            if sum(grid[i+k][j+k] for k in range(3)) != 15:
                return False
            if sum(grid[i+2-k][j+k] for k in range(3)) != 15:
                return False
            nums = []
            for r in range(3):
                for c in range(3):
                    nums.append(grid[i+r][j+c])
            for i in range(1, 10):
                if i not in nums:
                    return False
            return True

        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m-2):
            for j in range(n-2):
                if is_magic(i, j):
                    ans +=1
        return ans