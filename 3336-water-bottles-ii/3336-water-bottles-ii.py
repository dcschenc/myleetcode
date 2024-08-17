class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans, empty_bottles = 0, 0
        while numBottles > 0:
            ans += numBottles
            empty_bottles += numBottles
            numBottles = 0
            while empty_bottles >= numExchange:
                numBottles += 1
                empty_bottles -= numExchange
                numExchange += 1
        return ans
            