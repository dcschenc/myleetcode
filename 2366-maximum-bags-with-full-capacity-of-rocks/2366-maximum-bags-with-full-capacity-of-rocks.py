class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        to_filled = [0] * n
        for i in range(n):
            to_filled[i] = capacity[i] - rocks[i]
        to_filled.sort()
        for i in range(n):
            if to_filled[i] <= additionalRocks:
                additionalRocks -= to_filled[i]
            else:
                return i
        return n
            