from heapq import heappush, heappop
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        
        # Initialize the heap with the smallest fractions (arr[0] / arr[j], j > 0)
        for j in range(1, n):
            heapq.heappush(heap, (arr[0] / arr[j], 0, j))
        
        # Extract the smallest fractions k times
        for _ in range(k - 1):
            frac, i, j = heapq.heappop(heap)
            # Push the next fraction (arr[i+1] / arr[j]) if possible
            if i + 1 < j:
                heapq.heappush(heap, (arr[i+1] / arr[j], i + 1, j))
        
        # The k-th fraction
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]


        # n = len(arr)
        # heap = []
        # for i in range(n):
        #     for j in range(i+1, n):
        #         heapq.heappush(heap, (-arr[i]/arr[j], [arr[i], arr[j]]))
        #         if len(heap) > k:
        #             heapq.heappop(heap)
        # return heap[0][1]