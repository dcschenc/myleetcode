class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_load(c):
            if max(weights) > c:
                return False
            i, cnt, n = 0, 0, len(weights)
            while i < n:
                cur = weights[i]
                j = i + 1
                while j < n and cur + weights[j] <= c:
                    cur += weights[j]
                    j += 1
                    
                cnt += 1
                i = j
            return cnt <= days
            # if cnt > days:
            #     return False
            # return True
        
        lo, hi = 1, sum(weights)
        while lo <= hi:
            mid = (lo + hi)//2
            res = can_load(mid)
            if res:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo