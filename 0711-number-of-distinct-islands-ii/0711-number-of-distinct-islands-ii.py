class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        # Depth-First Search function to explore an island and record its shape
        def dfs(row, col, shape):
            shape.append((row, col))
            grid[row][col] = 0  # Mark the land as visited
            # Explore all 4 directions: up, down, left, right
            for delta_row, delta_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + delta_row, col + delta_col
                if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == 1:
                    dfs(new_row, new_col, shape)

        # Function to normalize the shapes by considering all 8 transformations
        def normalize(shape):
            # Create 8 transformations for each shape
            all_transformations = [[] for _ in range(8)]
            for x, y in shape:
                all_transformations[0].append((x, y))
                all_transformations[1].append((x, -y))
                all_transformations[2].append((-x, y))
                all_transformations[3].append((-x, -y))
                all_transformations[4].append((y, x))
                all_transformations[5].append((y, -x))
                all_transformations[6].append((-y, x))
                all_transformations[7].append((-y, -x))
          
            # Normalize by sorting and then subtracting the first pair to bring to origin
            for transformation in all_transformations:
                transformation.sort()
                origin_x, origin_y = transformation[0]
                for i in range(len(transformation)):
                    transformation[i] = (transformation[i][0] - origin_x, transformation[i][1] - origin_y)
          
            # Sort the transformations and keep the first one to represent this shape
            all_transformations.sort()
            return tuple(all_transformations[0])

        # Initialize variables and a set to store unique island shapes
        num_rows, num_cols = len(grid), len(grid[0])
        unique_islands = set()
      
        # Iterate over each cell in the grid
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col]:  # If the cell is a land
                    shape = []
                    dfs(row, col, shape)  # Perform DFS to get the shape of the island
                    unique_islands.add(normalize(shape))  # Normalize and add to set of unique islands
      
        # Return the number of unique island shapes
        return len(unique_islands)
