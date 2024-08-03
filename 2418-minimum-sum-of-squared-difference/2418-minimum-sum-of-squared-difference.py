class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int: 
        # https://algo.monster/liteproblems/2333
        k = k1 + k2
        diff_data = [abs(x - y) for x,y in zip(nums1, nums2)]
        left, right = 0, max(diff_data)      
        while left < right:
            mid = floor((left + right)//2)
            k_needed = sum([max(0, x - mid) for x in diff_data])
            if k_needed <= k:
                right = mid
            else:
                left = mid + 1
            
        if left == 0: 
            return 0
        else:
            a = sum([min(x, left)**2 for x in diff_data]) 
            b = (left**2 - (left-1)**2) * (k - sum([max(0, x - left) for x in diff_data]))
            return a - b


        # heaps = []
        # for a, b in zip(nums1, nums2):
        #     heappush(heaps, -abs(a - b))
        # i, n = 0, k1 + k2
        # while i < n:
        #     # print(heaps, i)
        #     cur = -heappop(heaps)
        #     if cur == 0: return 0
        #     nxt = -heaps[0]
        #     diff = max(cur - nxt, 1)
        #     i += diff
        #     heappush(heaps, -(cur - diff))
        # return int(sum([v ** 2 for v in heaps]))
