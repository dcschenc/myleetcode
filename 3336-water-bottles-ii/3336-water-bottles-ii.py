class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3100.Water%20Bottles%20II
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
            