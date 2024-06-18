class Solution:
    def totalNQueens(self, n: int) -> int:      
        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1                
                return
            for col in range(n):
                if is_valid(row, col):
                    chestboard[row][col] = 'Q'
                    backtrack(row + 1)
                    chestboard[row][col] = '.'
        
        def is_valid(row, col):
            for i in range(row):
                if chestboard[i][col] == 'Q':
                    return False
            i, j = row - 1, col - 1
            #### 45 direction ####
            while i >= 0 and j >= 0:
                if chestboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i, j = row - 1, col + 1
            ### 135 direction ####
            while i >= 0 and j < n:
                if chestboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True        

        count = 0
        chestboard = [['.'] * n for i in range(n)]
        backtrack(0)
        return count


        def backtrack(row, count):
            for col in range(n):
                # iterate through columns at the curent row.
                if grid[row][col] == -1:
                    # explore this partial candidate solution, and mark the attacking zone
                    place_queen(row, col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                    else:
                        # we move on to the next row
                        count = backtrack(row + 1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(row, col)
            return count        

        def place_queen(row, col):            
            for i in range(row, n):
                grid[i][col] += 1
            for j in range(col, n):
                grid[row][j] += 1
            i, j = row+1, col-1
            while i < n and j > -1:
                grid[i][j] += 1
                i+=1
                j-=1           
            i, j = row+1, col+1
            while i < n and j < n:
                grid[i][j] += 1
                i+=1
                j+=1
                
            grid[row][col] = -1
        
        def remove_queen(row, col):
            for i in range(row, n):
                grid[i][col] -=1
            for j in range(col, n):
                grid[row][j] -=1
            i, j = row+1, col-1
            while i < n and j > -1:
                grid[i][j] -=1
                i+=1
                j-=1            
            i, j = row+1, col+1
            while i < n and j < n:
                grid[i][j] -=1
                i+=1
                j+=1            
            grid[row][col] = -1
            
        grid = [[-1 for i in range(n)] for j in range(n)]
        # print(grid)
        
        return backtrack(0, 0)