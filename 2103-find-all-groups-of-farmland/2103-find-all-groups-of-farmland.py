class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if (
                    land[i][j] == 0
                    or (j > 0 and land[i][j - 1] == 1)
                    or (i > 0 and land[i - 1][j] == 1)
                ):
                    continue
                x, y = i, j
                while x + 1 < m and land[x + 1][j] == 1:
                    x += 1
                while y + 1 < n and land[x][y + 1] == 1:
                    y += 1
                ans.append([i, j, x, y])
        return ans

        
        # Get the dimensions of the input grid.
        m, n = len(land), len(land[0])
      
        # Initialize an output list to store the coordinates of each farmland.
        farmlands = []
      
        # Iterate over each cell in the grid.
        for row in range(m):
            for col in range(n):
                # Skip the cell if it is not part of a farmland, or if it is not the top-left cell 
                # of a farmland (if it's a continuation of a row or column of a previous farmland).
                if (land[row][col] == 0 or col > 0 and land[row][col - 1] == 1) or (row > 0 and land[row - 1][col] == 1):
                    continue

                # Initialize farmland boundaries with the current cell.
                end_row, end_col = row, col

                # Expand vertically downwards to find the bottom boundary of the farmland.
                while end_row + 1 < m and land[end_row + 1][col] == 1:
                    end_row += 1

                # Expand horizontally rightwards to find the right boundary of the farmland.
                while end_col + 1 < n and land[end_row][end_col + 1] == 1:
                    end_col += 1

                # Add the found farmland coordinates to the list.
                # It includes the top-left and bottom-right coordinates of the rectangle.
                farmlands.append([row, col, end_row,end_col])
              
                # Mark the found farmland on the map to not count it again
                for i in range(row, farmland_end_row + 1):
                    for j in range(col, farmland_end_col + 1):
                        land[i][j] = 0
                      
        # Return the list of coordinates for all farmlands found.
        return farmlands
