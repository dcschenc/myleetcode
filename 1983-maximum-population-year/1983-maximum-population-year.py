class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1854.Maximum%20Population%20Year
        d = [0] * 101
        offset = 1950
        for a, b in logs:
            a, b = a - offset, b - offset
            d[a] += 1
            d[b] -= 1
        s = mx = j = 0
        for i, x in enumerate(d):
            s += x
            if mx < s:
                mx, j = s, i
        return j + offset

        # year_start, year_end = 0, -float('inf')
        # m, n = len(logs), len(logs[0])
        # for i in range(m):
        #     year_sart = min(logs[i][0], year_start)
        #     year_end = max(logs[i][1], year_end)
        # population = -1
        # for year in range(year_start, year_end+1):
        #     cnt = 0
        #     for i in range(m):
        #         if year >= logs[i][0] and logs[i][1] > year:
        #             cnt += 1
        #     if cnt > population:
        #         population = cnt
        #         ans = year
        # return ans