class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])
        horizontalCuts.sort()
        verticalCuts.sort()
        max_width = max(b - a for a, b in pairwise(verticalCuts))
        max_height = max(b - a for a, b in pairwise(horizontalCuts))
        return max_width * max_height % (10 ** 9 + 7)