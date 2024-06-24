class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        # Sort the intervals based on their ending points
        points.sort(key=lambda x: x[1])
        arrows = 1  # Initialize the number of arrows to 1 (for the first balloon)
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                # If the current balloon's start is beyond the current arrow's end, a new arrow is needed
                arrows += 1
                end = points[i][1]
        return arrows