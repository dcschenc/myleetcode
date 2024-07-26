class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1891.Cutting%20Ribbons
        def can_cut(length):
            cnt = 0
            for r in ribbons:
                cnt += r // length
            return cnt >= k
           

        lo, hi = 1, max(ribbons)
        while lo <= hi:
            mid = (lo + hi) // 2
            res = can_cut(mid)
            if res:
                lo = mid + 1            
            else:
                hi = mid - 1
        return lo - 1