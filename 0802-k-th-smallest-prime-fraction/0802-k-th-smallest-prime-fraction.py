import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []  # Min heap to store fractions (value, numerator, denominator)

        for i in range(n - 1):
            heapq.heappush(min_heap, (arr[i] / arr[n - 1], i, n - 1))

        for _ in range(k - 1):
            value, numerator, denominator = heapq.heappop(min_heap)

            if numerator < denominator - 1:
                heapq.heappush(min_heap, (arr[numerator] / arr[denominator - 1], numerator, denominator - 1))

        return arr[min_heap[0][1]], arr[min_heap[0][2]]

        n = len(arr)
        heap = []
        for i in range(n):
            for j in range(i+1, n):
                heapq.heappush(heap, (-arr[i]/arr[j], [arr[i], arr[j]]))
                if len(heap) > k:
                    heapq.heappop(heap)
        return heap[0][1]