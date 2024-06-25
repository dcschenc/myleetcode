class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] >= timeSeries[i-1] + duration:
                res += duration
            else:
                res += timeSeries[i] - timeSeries[i-1]
        return res + duration
