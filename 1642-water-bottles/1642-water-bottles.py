class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            drinks = numBottles//numExchange 
            numBottles = drinks + numBottles % numExchange
            ans += drinks
        return ans