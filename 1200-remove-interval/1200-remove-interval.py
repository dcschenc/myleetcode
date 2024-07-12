class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        intervals.sort()
        ans = []
        start, end = toBeRemoved
        for s, e in intervals:
            if e < start or s > end:
                ans.append([s, e])
            else:
                if s < start:
                    ans.append([s, start])
                if e > end:
                    ans.append([end, e])
        return ans

