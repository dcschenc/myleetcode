class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1642.Furthest%20Building%20You%20Can%20Reach
        ladder_alloc = []
        n = len(heights)
        for i in range(n-1):
            d = heights[i + 1] - heights[i]
            if d <= 0:
                continue
            heappush(ladder_alloc, d)
            if len(ladder_alloc) > ladders:                
                bricks -= heappop(ladder_alloc)
                if bricks < 0:
                    return i
        return len(heights) - 1