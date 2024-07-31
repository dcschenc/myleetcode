class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2139.Minimum%20Moves%20to%20Reach%20Target%20Score
        if target == 1:
            return 0
        if maxDoubles == 0:
            return target - 1
        if target % 2 == 0 and maxDoubles:
            return 1 + self.minMoves(target >> 1, maxDoubles - 1)
        return 1 + self.minMoves(target - 1, maxDoubles)