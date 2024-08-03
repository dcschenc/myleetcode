class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2352.Equal%20Row%20and%20Column%20Pairs
        n = len(grid)
        hm = {}
        for i in range(n):
            key = tuple(grid[i])
            if key not in hm:
                hm[key] = 1
            else:
                hm[key] +=1
        count = 0
        for i in range(n):
            key = []
            for j in range(n):
                key.append(grid[j][i])
            key = tuple(key)
            if key in hm:
                count += hm[key]
        return count