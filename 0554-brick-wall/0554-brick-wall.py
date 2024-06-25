class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # https://algo.monster/liteproblems/554
        # Create a dictionary to count the frequency of each edge's position (except for the last edge of each row)
        edge_count = defaultdict(int)
      
        # Iterate over each row in the wall
        for row in wall:
            width = 0  # Initialize width to track the current position of edges
          
            # Iterate over each brick in the row, except the last brick
            for brick in row[:-1]:
                width += brick  # Increase the width by the current brick's length to find the next edge
                edge_count[width] += 1  # Increment the count of the edge at the corresponding width
          
        # If there are no edges counted, return the number of rows (since a vertical line would cross all rows)
        if not edge_count:
            return len(wall)
      
        # Find the maximum occurrence of a common edge and subtract it from the total rows.
        # This gives the minimum number of rows crossed by a vertical line.
        return len(wall) - max(edge_count.values())
