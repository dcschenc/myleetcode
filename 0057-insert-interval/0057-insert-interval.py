class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/0000-0099/0057.Insert%20Interval
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort()
            ans = [intervals[0]]
            for s, e in intervals[1:]:
                if ans[-1][1] < s:
                    ans.append([s, e])
                else:
                    ans[-1][1] = max(ans[-1][1], e)
            return ans

        intervals.append(newInterval)
        return merge(intervals)
        
        # n = len(intervals)
        # i = 0
        # res = []

        # # Case 1: No overlapping before merging intervals
        # while i < n and intervals[i][1] < newInterval[0]:
        #     res.append(intervals[i])
        #     i += 1

        # # Case 2: Overlapping and merging intervals
        # while i < n and newInterval[1] >= intervals[i][0]:
        #     newInterval[0] = min(newInterval[0], intervals[i][0])
        #     newInterval[1] = max(newInterval[1], intervals[i][1])
        #     i += 1
        # res.append(newInterval)

        # # Case 3: No overlapping after merging newInterval
        # while i < n:
        #     res.append(intervals[i])
        #     i += 1

        # return res