class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:  
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2510.Check%20if%20There%20is%20a%20Path%20With%20Equal%20Number%20of%200's%20And%201's
        @cache
        def dfs(i, j, k):
            if i == m - 1 and j == n - 1:
                return k == s    

            k += grid[i][j]         
            ans = False
            if i + 1 < m:
                ans |= dfs(i + 1, j, k)
            if j + 1 < n:
                ans |= dfs(i, j + 1, k)            
            return ans

        m, n = len(grid), len(grid[0])
        s = m + n - 1
        if s & 1:
            return False
        s >>= 1
        return dfs(0, 0, 0)

        # @cache 
        # def dfs(x, y, zero, one):
        #     if x == m - 1 and y == n - 1:
        #         if zero == one:
        #             return True
        #         return False
        #     ans = False
        #     if x + 1 < m:
        #         if grid[x + 1][y] == 0:
        #             ans |= dfs(x + 1, y, zero + 1, one)
        #         else:
        #             ans |= dfs(x + 1, y, zero, one + 1)
        #     if y + 1 < n:
        #         if grid[x][y + 1] == 0:
        #             ans |= dfs(x, y + 1, zero + 1, one)
        #         else:
        #             ans |= dfs(x, y + 1, zero, one + 1)
        #     return ans
        
        # m, n = len(grid), len(grid[0])
        # if grid[0][0] == 0:
        #     return dfs(0, 0, 1, 0)
        # else:
        #     return dfs(0, 0, 0, 1)


        # def dfs(x, y, zero, one):
        #     if x == m - 1 and y == n - 1:
        #         if zero == one:
        #             return True
        #         return False
        #     ans = False
        #     if x + 1 < m:
        #         if grid[x + 1][y] == 0:
        #             ans |= dfs(x + 1, y, zero + 1, one)
        #         else:
        #             ans |= dfs(x + 1, y, zero, one + 1)
        #     if y + 1 < n:
        #         if grid[x][y + 1] == 0:
        #             ans |= dfs(x, y + 1, zero + 1, one)
        #         else:
        #             ans |= dfs(x, y + 1, zero, one + 1)
        #     return ans
        
        # m, n = len(grid), len(grid[0])
        # if grid[0][0] == 0:
        #     return dfs(0, 0, 1, 0)
        # else:
        #     return dfs(0, 0, 0, 1)

        # m, n = len(grid), len(grid[0])
        # queue = deque()
        # if grid[0][0] == 0:
        #     queue.append((0, 0, 1, 0))
        # else:
        #     queue.append((0, 0, 0, 1))
        # while queue:
        #     for _ in range(len(queue)):
        #         x, y, zero, one = queue.popleft()
        #         if x == m-1 and y == n-1:
        #             if zero == one:
        #                 return True                    
        #         if x + 1 < m:
        #             if grid[x + 1][y] == 0:                        
        #                 queue.append((x + 1, y, zero + 1, one))
        #             else:
        #                 queue.append((x + 1, y, zero, one + 1))
        #         if y + 1 < n:
        #             if grid[x][y + 1] == 0:
        #                 queue.append((x, y + 1, zero + 1, one))
        #             else:
        #                 queue.append((x, y + 1, zero, one + 1))
        # return False
