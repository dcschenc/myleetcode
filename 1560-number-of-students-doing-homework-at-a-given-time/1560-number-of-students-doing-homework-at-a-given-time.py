class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        i, n = 0, len(startTime)
        ans = 0
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                ans += 1
        return ans