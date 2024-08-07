class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2580.Count%20Ways%20to%20Group%20Overlapping%20Ranges
        ranges.sort()
        cnt, mx = 0, -1
        for start, end in ranges:
            if start > mx:
                cnt += 1
            mx = max(mx, end)
        mod = 10 ** 9 + 7
        return pow(2, cnt, mod)