class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0 
        h_set = set(jewels)
        for c in stones:
            if c in h_set:
                count += 1
        return count
