class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2064.Minimized%20Maximum%20of%20Products%20Distributed%20to%20Any%20Store
        def can_distribute(x):
            m = len(quantities)
            cnt, i = 0, 0
            while i < m:
                cnt += math.ceil(quantities[i] / x)
                i += 1
            return cnt <= n            
        
        lo, hi = 1, sum(quantities)
        while lo <= hi:
            mid = (lo + hi) // 2
            res = can_distribute(mid)
            if res:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo