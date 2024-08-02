class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_distribute(x):
            cnt = 0
            for i in range(len(candies)):
                cnt += candies[i] // x
            return cnt >= k

        if sum(candies) < k:
            return 0
        lo, hi = 1, max(candies)
        while lo <= hi:
            mid = (lo + hi) // 2
            res = can_distribute(mid)
            if res:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo - 1