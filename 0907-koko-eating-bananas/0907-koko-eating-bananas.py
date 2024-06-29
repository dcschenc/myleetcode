class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/k)
            return hours <= h

        low, high = 1, max(piles)
        res = high
        while low <= high:
            mid = (low + high)//2
            finished = can_finish(mid)
            if finished:
                high = mid - 1
                res = min(res, mid)
            else:
                low = mid + 1
        return res
        # if can_finish(mid):        
        #     return mid
        # else:
        #     return mid + 1