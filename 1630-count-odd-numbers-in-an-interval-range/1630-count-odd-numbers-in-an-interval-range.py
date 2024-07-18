class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds = (high - low + 1)//2
        if low % 2 == 1 and high % 2 == 1:
            odds += 1
        
        return odds