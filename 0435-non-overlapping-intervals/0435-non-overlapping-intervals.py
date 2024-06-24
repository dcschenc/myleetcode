class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ans, end = 0, -inf
        for cur in intervals:
            if cur[0] >= end:
                end = cur[1]
            else:
                ans += 1
        return ans

        # intervals.sort(key = lambda x: (x[0], x[1]))  ### can not sort by x[0], image [1, 100000000000], [2, 3], [3, 4]
        # ans = 0
        # prev = intervals[0]
        # print(intervals)
        # for cur in intervals[1:]:
        #     if cur[0] < prev[1]:
        #         ans += 1
        #         print(cur)
        #     else:
        #         prev = cur
        # return ans


