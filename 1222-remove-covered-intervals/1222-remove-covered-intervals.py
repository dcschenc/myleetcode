class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        l, ans = 0, 0
        for i in range(1, len(intervals)):
            if intervals[i][1] > intervals[l][1]:
                l = i
            else:
                ans += 1 
        return len(intervals) - ans
        