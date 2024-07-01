class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
        return points[:k]
        
        min_heap = []
        for x, y in points:
            dis = -(x*x + y*y)  ### 用负数 ###         
            heapq.heappush(min_heap, (dis, [x, y]))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [x[1] for x in min_heap]