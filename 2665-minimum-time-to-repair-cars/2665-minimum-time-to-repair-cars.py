class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2594.Minimum%20Time%20to%20Repair%20Cars
        def can_repair(t):
            cnt = 0
            for r in ranks:
                cnt += math.floor(math.sqrt(t / r))
            return cnt >= cars

        lo, hi = 0, 10**14
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_repair(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo