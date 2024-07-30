class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2128.Remove%20All%20Ones%20With%20Row%20and%20Column%20Flips
        s = set()
        for row in grid:
            cur = tuple(row) if row[0] == grid[0][0] else tuple([x ^ 1 for x in row])
            s.add(cur)
        return len(s) == 1