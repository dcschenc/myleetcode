class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # Initialize the surface area to 0
        surface_area = 0
      
        # Loop through each cell of the grid
        for i, row in enumerate(grid):
            for j, height in enumerate(row):
                # If the height of the current voxel is not zero
                if height:
                    # Add the surface area of the current voxel
                    # Each voxel contributes to 2 base/top faces and 4 side faces
                    surface_area += 2 + height * 4

                    # If we are not on the first row, subtract the overlapping area
                    # with the voxel directly behind (in the i-1 row)
                    if i:
                        surface_area -= min(height, grid[i - 1][j]) * 2

                    # If we are not in the first column, subtract the overlapping area
                    # with the voxel directly on the left (in the j-1 column)
                    if j:
                        surface_area -= min(height, grid[i][j - 1]) * 2

        # Return the total calculated surface area
        return surface_area