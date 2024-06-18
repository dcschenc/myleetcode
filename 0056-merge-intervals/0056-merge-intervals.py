class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        n = len(intervals)
        # print(intervals)
        i = 1
        while i < n:
            cur = res[-1]
            if cur[1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                # will pass intervals[i] & use curr instead
                # if cur[1] < intervals[i][1]:
                #     cur[1] = intervals[i][1]
                cur[1] = max(cur[1], intervals[i][1])
            i += 1
        return res