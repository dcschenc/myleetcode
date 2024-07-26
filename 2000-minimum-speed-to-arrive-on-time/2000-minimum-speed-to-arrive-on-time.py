class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1870.Minimum%20Speed%20to%20Arrive%20on%20Time
        def can_reach(x):
            cnt = 0
            for i in range(n):
                if i == n - 1:
                    cnt += dist[i] / x
                else:
                    cnt += math.ceil(dist[i] / x)
            return cnt <= hour           
        
        lo, hi = 1, 2**32 - 1
        n = len(dist)
        if n -1 >= hour:
            return -1        
        while lo <= hi:
            mid = (lo + hi) // 2
            res = can_reach(mid)
            if res:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo