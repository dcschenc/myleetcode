class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2187.Minimum%20Time%20to%20Complete%20Trips
        def can_finish(t):
            cnt = 0
            for i in range(len(time)):
                cnt += t // time[i]
            return cnt >= totalTrips     
        
        lo, hi = 0, min(time) * totalTrips
        while lo <= hi:
            mid = (lo + hi) // 2
            res = can_finish(mid)
            if res:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo