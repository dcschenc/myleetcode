class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1851.Minimum%20Interval%20to%20Include%20Each%20Query
        # Sort intervals by their starting points
        intervals.sort(key=lambda x: x[0])
        # Sort queries and keep track of their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        result = [-1] * len(queries)
        min_heap = []
        i = 0
        
        for idx, query in sorted_queries:
            # Add all intervals that can start before or at the query point
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(min_heap, (end - start + 1, end))
                i += 1
            
            # Remove all intervals that cannot include the query point
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # The smallest interval that includes the query point is on the top of the heap
            if min_heap:
                result[idx] = min_heap[0][0]
        
        return result