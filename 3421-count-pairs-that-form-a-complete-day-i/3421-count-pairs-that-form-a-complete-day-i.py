class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
       return sum((a + b) % 24 == 0 for a, b in combinations(hours, 2))
