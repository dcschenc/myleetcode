class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0857.Minimum%20Cost%20to%20Hire%20K%20Workers
        # Pair each worker's quality with their minimum wage 
        # and sort the workers based on their wage-to-quality ratio.
        workers = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
      
        # Initialize the answer as infinity to be later minimized
        # Initialize the total quality of workers hired so far as zero
        min_cost = float('inf')
        total_quality = 0
      
        # Max heap to store the negative of qualities, 
        # since heapq in Python is a min heap by default
        max_heap = []
      
        # Iterate over each worker
        for q, w in workers:
            # Add the current worker's quality to the total quality
            total_quality += q
            # Push the negative quality to the heap
            heapq.heappush(max_heap, -q)
          
            # If we have more than k workers, remove the one with the highest quality
            if len(max_heap) > k:
                # Since we stored negative qualities, popping from heap retrieves
                # and removes the biggest quality from the total
                total_quality += heapq.heappop(max_heap)
          
            # If we've collected a group of k workers
            if len(max_heap) == k:
                # Calculate the current cost for this group of workers, which is
                # the wage-to-quality ratio of the current worker times total quality
                # and update the minimum cost if it's less than the previous minimum
                min_cost = min(min_cost, w / q * total_quality)
      
        # Return the minimum cost found to hire k workers
        return min_cost
        
        
        t = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
        ans, tot = inf, 0
        h = []
        for q, w in t:
            tot += q
            heappush(h, -q)
            if len(h) == k:
                ans = min(ans, w / q * tot)
                tot += heappop(h)  # 减去之前的工作量
        return ans

        workers = sorted((w / q, q) for w, q in zip(wage, quality))
        heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(heap, -q)
            total_quality += q

            if len(heap) > k:
                total_quality += heapq.heappop(heap)  # 减去之前的工作量

            if len(heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost        