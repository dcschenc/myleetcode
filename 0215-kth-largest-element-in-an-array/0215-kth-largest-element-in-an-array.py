import heapq
from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        # print(heap)
        for i in range(k, len(nums)):
            # heapq.heappushpop(heap, nums[i])
            heappush(heap, nums[i])
            heappop(heap)
        return heapq.heappop(heap)