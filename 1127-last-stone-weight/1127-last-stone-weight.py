class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, y-x)
        return -stones[0] if stones else 0
            