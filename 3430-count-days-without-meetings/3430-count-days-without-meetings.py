class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[0], -x[1]))
        n = len(meetings)
        start, end = meetings[0]
        ans = start - 1
        for i in range(1, n):
            cur_start, cur_end = meetings[i]
            ans += max(0, cur_start - end - 1)
            start, end = cur_start, max(cur_end, end)
        ans += max(0, days - end)
        return ans