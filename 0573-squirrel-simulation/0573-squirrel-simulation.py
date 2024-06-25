class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # x, y, a, b = *tree, *squirrel
        (x, y), (a, b) = tree, squirrel
        total = sum(abs(i - x) + abs(j - y) for i, j in nuts) * 2
        ans = inf
        for i, j in nuts:
            c = abs(i - x) + abs(j - y)
            d = abs(i - a) + abs(j - b) + c
            ans = min(ans, total + d - c * 2)
        return ans