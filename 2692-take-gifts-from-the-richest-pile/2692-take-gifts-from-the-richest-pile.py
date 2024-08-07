class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2558.Take%20Gifts%20From%20the%20Richest%20Pile
        h = [-v for v in gifts]
        heapify(h)
        for _ in range(k):
            heapreplace(h, -int(sqrt(-h[0])))
        return -sum(h)

        # # total = sum(gifts)
        # heaps = []
        # for g in gifts:
        #     heappush(heaps, -g)
        # cur = 0
        # while k > 0:
        #     cur = -heappop(heaps)            
        #     heappush(heaps, -math.floor(sqrt(cur)))
        #     k -= 1
        # return -sum(heaps)
